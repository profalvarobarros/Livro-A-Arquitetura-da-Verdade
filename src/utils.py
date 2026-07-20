"""
Utilitários compartilhados por todos os notebooks do livro
"A Saga da Classificação".

Objetivo: garantir que todo capítulo parta exatamente do mesmo estado
(mesma seed, mesmo split, mesmos artefatos) para que os números citados
no texto do livro sejam reproduzíveis capítulo a capítulo.
"""

import os
import random
import pickle
import json

import numpy as np

_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def set_seed(seed: int = 42) -> None:
    """Fixa a seed em todas as bibliotecas relevantes.

    Chamar sempre na primeira célula de cada notebook, antes de
    qualquer split, shuffle ou inicialização de modelo. Sem isso,
    os números reportados no livro não são reproduzíveis entre
    execuções, quanto mais entre capítulos.
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)


def save_artifact(obj, name: str, chapter: int) -> str:
    """Salva um artefato (dataset, split, modelo treinado, métricas)
    em _data/, prefixado pelo capítulo que o gerou.

    Exemplo: save_artifact(X_train, "X_train", chapter=4)
    -> _data/cap04_X_train.pkl
    """
    os.makedirs(_DATA_DIR, exist_ok=True)
    path = os.path.join(_DATA_DIR, f"cap{chapter:02d}_{name}.pkl")
    with open(path, "wb") as f:
        pickle.dump(obj, f)
    return path


def load_artifact(name: str, chapter: int):
    """Carrega um artefato salvo por um capítulo anterior.

    Exemplo: X_train = load_artifact("X_train", chapter=4)
    """
    path = os.path.join(_DATA_DIR, f"cap{chapter:02d}_{name}.pkl")
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Artefato '{name}' do Capítulo {chapter} não encontrado em {path}. "
            f"Rode o notebook do Capítulo {chapter} primeiro (ou baixe os artefatos "
            f"pré-gerados, ver README de codigo/)."
        )
    with open(path, "rb") as f:
        return pickle.load(f)


def save_metrics(metrics: dict, chapter: int) -> str:
    """Salva métricas de um capítulo em JSON, para o Capítulo 29
    (comparação de modelos) consolidar depois."""
    os.makedirs(_DATA_DIR, exist_ok=True)
    path = os.path.join(_DATA_DIR, f"metrics_cap{chapter:02d}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)
    return path


def load_all_metrics() -> dict:
    """Usado pelo Capítulo 29 para montar a tabela comparativa final."""
    result = {}
    if not os.path.isdir(_DATA_DIR):
        return result
    for fname in sorted(os.listdir(_DATA_DIR)):
        if fname.startswith("metrics_cap") and fname.endswith(".json"):
            with open(os.path.join(_DATA_DIR, fname), encoding="utf-8") as f:
                result[fname] = json.load(f)
    return result
