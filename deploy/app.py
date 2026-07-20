"""
app.py — API de inferência do OncoClassify 2.0 (Capítulo 25 — Deployment).

Expõe o modelo final como um serviço web com FastAPI. Recebe um dicionário
nomeado de features (não uma lista posicional, para evitar erros silenciosos
de ordenação) e devolve o diagnóstico com as probabilidades associadas.

Uso:
    uvicorn deploy.app:app --reload
    # depois, abra http://127.0.0.1:8000/docs para testar o endpoint /prever
"""
import os

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

_MODELO_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "oncoclassify_v2.pkl")
modelo = joblib.load(_MODELO_PATH)

# Os nomes e a ordem das features vêm do próprio modelo — robustez por construção.
FEATURES = list(modelo.feature_names_in_)

app = FastAPI(
    title="OncoClassify API",
    version="2.0",
    description="Serviço de apoio à decisão para triagem de tumores mamários "
                 "a partir de features morfológicas do Wisconsin Breast Cancer "
                 "Dataset. Material didático — ver aviso legal no README.",
)


class Paciente(BaseModel):
    features: dict[str, float]


@app.post("/prever")
def prever(dados: Paciente):
    try:
        entrada = pd.DataFrame([dados.features])[FEATURES]  # reordena pela ordem do modelo
        prob = modelo.predict_proba(entrada)[0]
        return {
            "diagnostico": "Maligno" if prob[0] >= 0.5 else "Benigno",
            "probabilidade_maligno": round(float(prob[0]), 4),
            "probabilidade_benigno": round(float(prob[1]), 4),
        }
    except KeyError as e:
        return {"erro": f"feature ausente: {e}"}


@app.get("/")
def raiz():
    return {
        "servico": "OncoClassify API",
        "versao": "2.0",
        "endpoint": "/prever (POST)",
        "docs": "/docs",
        "aviso": "Uso educacional. Não é um dispositivo médico certificado.",
    }
