"""
oncoclassify_utils.py — Módulo central do projeto OncoClassify 2.0
==================================================================
"A Arquitetura da Verdade — A Saga da Classificação"

Ponto único de verdade do livro (princípio DRY). Centraliza constantes,
grupos de colunas, o dataset bruto (para ensino), a curadoria transparente,
a base canônica de modelagem e a "separação sagrada" treino/teste.

Convenção de rótulo (fixa no livro todo):  0 = Maligno  |  1 = Benigno
A classe POSITIVA de interesse clínico é a Maligna (0).
"""

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, recall_score

# ----------------------------------------------------------------------
# 1. CONSTANTES DO PROJETO
# ----------------------------------------------------------------------
RANDOM_STATE = 42     # semente única — reprodutibilidade em todo o livro
TEST_SIZE    = 0.20   # 20% guardados no "cofre" até a avaliação final
CUSTO_FN     = 100    # custo relativo de um Falso Negativo (câncer não detectado)
CUSTO_FP     = 10     # custo relativo de um Falso Positivo (alarme falso)

# ----------------------------------------------------------------------
# 2. GRUPOS DE COLUNAS DO DATASET MODIFICADO
# ----------------------------------------------------------------------
FEATURES_MORFOLOGICAS = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area',
    'mean smoothness', 'mean compactness', 'mean concavity',
    'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error',
    'smoothness error', 'compactness error', 'concavity error',
    'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area',
    'worst smoothness', 'worst compactness', 'worst concavity',
    'worst concave points', 'worst symmetry', 'worst fractal dimension',
]

# Identificadores administrativos — NÃO são preditores; correlação espúria.
COLUNAS_ID = ['patient code', 'scan_id', 'session code']

# Vazamento de alvo (data leakage): derivadas do diagnóstico. Se entrarem no
# modelo, produzem acurácia ~100% FRAUDULENTA. Lição central do Capítulo 4.
COLUNAS_LEAKAGE = ['diagnosis progression score', 'post evaluation flag']

# Clínicas legítimas, porém fracas/problemáticas. Servem à narrativa de
# limpeza (Caps. 1–5); descartadas da base de modelagem com justificativa.
COLUNAS_CLINICAS = ['patient age', 'patient gender', 'family history',
                    'biopsy time', 'genetic test result']

# ----------------------------------------------------------------------
# 3. CARGA DO DATASET BRUTO
# ----------------------------------------------------------------------
_URL_PUBLICA = ("https://raw.githubusercontent.com/profalvarobarros/"
                "Livro-A-Arquitetura-da-Verdade/refs/heads/main/"
                "WisconsinBreastCancerDataset_MODIFIED.csv")
_CSV_LOCAL = Path(__file__).resolve().parent.parent / "data" / \
             "WisconsinBreastCancerDataset_MODIFIED.csv"


def carregar_dataset_bruto():
    """Retorna o dataset modificado COMO ELE VEM (com problemas de qualidade)."""
    caminho = _CSV_LOCAL if _CSV_LOCAL.exists() else _URL_PUBLICA
    return pd.read_csv(caminho)


# ----------------------------------------------------------------------
# 4. CURADORIA — transparente e reexecutável
# ----------------------------------------------------------------------
def limpar_dataset(df_bruto, retornar_relatorio=False):
    """Transforma o dataset bruto na base canônica de modelagem."""
    df = df_bruto.copy()
    n_inicial = len(df)

    df = df.drop_duplicates().reset_index(drop=True)
    n_duplicatas = n_inicial - len(df)

    df['target'] = df['target'].map({'M': 0, 'B': 1})

    base = df[FEATURES_MORFOLOGICAS + ['target']].copy()
    base['diagnosis_label'] = base['target'].map({0: 'Maligno', 1: 'Benigno'})

    if retornar_relatorio:
        relatorio = {
            'linhas_brutas': n_inicial,
            'duplicatas_removidas': n_duplicatas,
            'linhas_canonicas': len(base),
            'colunas_descartadas': COLUNAS_ID + COLUNAS_LEAKAGE + COLUNAS_CLINICAS,
            'features_modelo': len(FEATURES_MORFOLOGICAS),
        }
        return base, relatorio
    return base


# ----------------------------------------------------------------------
# 5. BASE CANÔNICA E A "SEPARAÇÃO SAGRADA" (fixas no livro todo)
# ----------------------------------------------------------------------
df_raw  = carregar_dataset_bruto()          # sujo — só para ensino (Caps. 1–4)
df_full = limpar_dataset(df_raw)            # base canônica de modelagem (600×30)

X = df_full[FEATURES_MORFOLOGICAS]
y = df_full['target']                        # 0 = Maligno, 1 = Benigno

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)

# ----------------------------------------------------------------------
# 6. VISUALIZAÇÃO — paleta e hachuras consistentes
# ----------------------------------------------------------------------
# Scorer canônico: recall da classe Maligna (0) — a métrica clínica central.
recall_maligno = make_scorer(recall_score, pos_label=0)


color_map   = {'Benigno': '#4C72B0', 'Maligno': '#C44E52'}
hatches_map = {'Benigno': '', 'Maligno': '//'}


def apply_hatches_bars(ax, class_order):
    for patch, classe in zip(ax.patches, class_order):
        patch.set_hatch(hatches_map.get(classe, ''))


def apply_hatches_boxplot(ax, class_order):
    n = max(len(class_order), 1)
    for i, patch in enumerate(ax.patches):
        try:
            patch.set_hatch(hatches_map.get(class_order[i % n], ''))
        except Exception:
            pass


def apply_hatches_violinplot(ax, class_order):
    n = max(len(class_order), 1)
    for i, coll in enumerate(ax.collections):
        try:
            coll.set_hatch(hatches_map.get(class_order[i % n], ''))
        except Exception:
            pass


def print_project_info():
    print("=" * 60)
    print("PROJETO ONCOCLASSIFY 2.0")
    print("   A Arquitetura da Verdade - A Saga da Classificacao")
    print("=" * 60)
    print(f"   RANDOM_STATE:      {RANDOM_STATE}")
    print(f"   TEST_SIZE:         {TEST_SIZE}")
    print(f"   CUSTO_FN:          {CUSTO_FN} (Falso Negativo)")
    print(f"   CUSTO_FP:          {CUSTO_FP} (Falso Positivo)")
    print(f"   Base canonica:     {df_full.shape[0]} amostras")
    print(f"   Features (modelo): {len(FEATURES_MORFOLOGICAS)} morfologicas")
    print(f"   Convencao alvo:    0 = Maligno | 1 = Benigno")
    print("=" * 60)
