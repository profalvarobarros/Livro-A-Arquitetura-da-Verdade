"""
treinar_modelo.py — pipeline de treino do artefato de produção.

Executa UMA vez para gerar 'oncoclassify_v2.pkl': o ensemble (Regressão
Logística + SVM + Gradient Boosting, votação soft) treinado nas 600 amostras
canônicas, conforme validado no Capítulo 24 ("O Julgamento Final") e
implantado no Capítulo 25 ("Deployment") de "A Arquitetura da Verdade".

Uso:
    python deploy/treinar_modelo.py
"""
import os
import sys

import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from oncoclassify_utils import X, y  # base canônica completa (600 amostras)

log = Pipeline([
    ("sc", StandardScaler()),
    ("lr", LogisticRegression(solver="liblinear", random_state=42)),
])
svm = Pipeline([
    ("sc", StandardScaler()),
    ("svm", SVC(kernel="rbf", C=10, gamma=0.01, probability=True, random_state=42)),
])
gb = GradientBoostingClassifier(n_estimators=100, random_state=42)

modelo_final = VotingClassifier([("lr", log), ("svm", svm), ("gb", gb)], voting="soft")
modelo_final.fit(X, y)  # treina em TODAS as 600 amostras, pós-avaliação do Cap. 24

destino = os.path.join(os.path.dirname(__file__), "..", "models", "oncoclassify_v2.pkl")
joblib.dump(modelo_final, destino)
print(f"Modelo treinado em {len(X)} amostras e salvo em '{destino}'")
