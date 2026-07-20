# A Arquitetura da Verdade — A Saga da Classificação

### Código-fonte oficial do livro

[![Python](https://img.shields.io/badge/Python-3.10.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-green.svg)](LICENSE)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-f89939.svg)](https://scikit-learn.org/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/profalvarobarros/Livro-A-Arquitetura-da-Verdade/blob/main/notebooks/capitulo_01_o_preco_da_certeza/capitulo_01.ipynb)

Este repositório contém todo o código do projeto didático **OncoClassify 2.0**
desenvolvido ao longo de *A Arquitetura da Verdade — A Saga da Classificação*,
segundo volume da trilogia **A Carta dos Modelos**, de **Alvaro Riz de Barros**.

> Este é um repositório de **código**, não do livro. Os notebooks trazem o
> contexto técnico necessário para acompanhar cada capítulo, mas a narrativa
> completa — incluindo a carta que dá início a esta saga — está disponível
> apenas na obra publicada. Ver [Licença](#licença) e [Sobre o livro](#sobre-o-livro).

---

## Sobre o livro

Um sistema de classificação com 97% de acurácia decidiu que o tumor de
Helena era benigno. Ele estava entre os 3% que erram. *A Arquitetura da
Verdade* parte desse erro para reconstruir, capítulo a capítulo, o
**OncoClassify**: um projeto de classificação binária aplicado ao diagnóstico
de câncer de mama, do primeiro dataframe sujo até um serviço em produção
com monitoramento, fairness e explicabilidade clínica.

Não é um livro sobre acertar métricas. É sobre o que significa, na prática,
transformar uma probabilidade em uma decisão que alguém vai viver — ou não.

**A trilogia "A Carta dos Modelos":**

| Volume | Título | Tema |
|---|---|---|
| 1 | *O Preço da Precisão* | Regressão — humildade científica diante da incerteza contínua |
| **2** | **A Arquitetura da Verdade** | **Classificação — o peso de decidir entre categorias** *(este repositório)* |
| 3 | *O Arquiteto do Amanhã* | Séries temporais — previsão com memória do tempo |

## Sobre este repositório

O texto do livro trata `X_train`, `X_test`, `y_train` e `y_test` como
constantes que atravessam do Capítulo 4 ao Capítulo 30 — cada capítulo parte
exatamente de onde o anterior parou. A estrutura deste repositório reflete
isso:

```
Livro-A-Arquitetura-da-Verdade/
├── notebooks/                    # um notebook por capítulo, ordem didática do livro
│   ├── capitulo_01_o_preco_da_certeza/
│   │   ├── capitulo_01.ipynb
│   │   └── media/                # figuras geradas pelo próprio notebook
│   ├── capitulo_02_a_anatomia_da_diferenca/
│   └── ...                       # 29 notebooks ao todo (ver sumário abaixo)
├── src/
│   ├── oncoclassify_utils.py     # módulo central do projeto (Apêndice E do livro)
│   └── utils.py                  # seed fixa + save_artifact/load_artifact entre capítulos
├── data/
│   ├── WisconsinBreastCancerDataset_MODIFIED.csv
│   └── README.md                 # proveniência e aviso de uso do dataset
├── models/
│   └── oncoclassify_v2.pkl       # artefato de produção (Capítulos 24-25)
├── deploy/
│   ├── treinar_modelo.py         # gera o artefato de produção
│   └── app.py                    # API FastAPI do Capítulo 25
├── requirements.txt
├── CITATION.cff
└── LICENSE
```

`src/oncoclassify_utils.py` é o "ponto único de verdade" do projeto: fixa
`RANDOM_STATE = 42`, os custos assimétricos de erro (`CUSTO_FN = 100`,
`CUSTO_FP = 10`), a curadoria do dataset bruto e o split treino/teste
estratificado que todos os capítulos compartilham. `src/utils.py` complementa
com `save_artifact` / `load_artifact`, para passar estado de um capítulo ao
próximo sem duplicar código nos notebooks.

## Como usar

### Opção 1 — Google Colab (nenhuma instalação)

Cada notebook é autossuficiente: abra pelo link "Open in Colab" no topo do
arquivo (ou clique no badge acima para começar pelo Capítulo 1) e rode as
células em ordem. O notebook busca `oncoclassify_utils.py` e o dataset
automaticamente.

### Opção 2 — Ambiente local

```bash
git clone https://github.com/profalvarobarros/Livro-A-Arquitetura-da-Verdade.git
cd Livro-A-Arquitetura-da-Verdade

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook notebooks/
```

Rode os notebooks **na ordem dos capítulos**: a partir do Capítulo 4, cada um
consome artefatos (`X_train`, modelos treinados, métricas) salvos pelos
capítulos anteriores em `data/`.

### Opção 3 — Subir a API de produção (Capítulo 25)

```bash
python deploy/treinar_modelo.py       # regenera models/oncoclassify_v2.pkl
uvicorn deploy.app:app --reload       # http://127.0.0.1:8000/docs
```

## Sumário de capítulos

| # | Capítulo | Tema técnico | Notebook |
|---|---|---|---|
| 1 | O Preço da Certeza | Regressão vs. classificação; primeiro contato com dados sujos | [`capitulo_01`](notebooks/capitulo_01_o_preco_da_certeza/capitulo_01.ipynb) |
| 2 | A Anatomia da Diferença | Formalização do problema de classificação binária | [`capitulo_02`](notebooks/capitulo_02_a_anatomia_da_diferenca/capitulo_02.ipynb) |
| 3 | O Dilema de Hipócrates | Falsos positivos vs. falsos negativos; custos assimétricos | [`capitulo_03`](notebooks/capitulo_03_o_dilema_de_hipocrates/capitulo_03.ipynb) |
| 4 | A Primeira Lei da Máquina | Separação treino/teste; detecção de *data leakage* | [`capitulo_04`](notebooks/capitulo_04_a_primeira_lei_da_maquina/capitulo_04.ipynb) |
| 5 | O Mapa do Terreno | Análise exploratória (EDA) para classificação | [`capitulo_05`](notebooks/capitulo_05_o_mapa_do_terreno/capitulo_05.ipynb) |
| 6 | Esculpindo o Sinal | *Feature engineering* orientada à decisão | [`capitulo_06`](notebooks/capitulo_06_esculpindo_o_sinal/capitulo_06.ipynb) |
| 7 | O Corte de Occam | *Feature selection* | [`capitulo_07`](notebooks/capitulo_07_o_corte_de_occam/capitulo_07.ipynb) |
| 8 | O Teorema de Bayes | Naive Bayes | [`capitulo_08`](notebooks/capitulo_08_o_teorema_de_bayes/capitulo_08.ipynb) |
| 9 | A Geometria da Separação | Support Vector Machines | [`capitulo_09`](notebooks/capitulo_09_a_geometria_da_separacao/capitulo_09.ipynb) |
| 10 | A Sabedoria das Árvores | Decision Trees | [`capitulo_10`](notebooks/capitulo_10_a_sabedoria_das_arvores/capitulo_10.ipynb) |
| 11 | Os Vizinhos que Decidem | K-Nearest Neighbors | [`capitulo_11`](notebooks/capitulo_11_os_vizinhos_que_decidem/capitulo_11.ipynb) |
| 12 | A Função Logística | Regressão logística | [`capitulo_12`](notebooks/capitulo_12_a_funcao_logistica/capitulo_12.ipynb) |
| 13 | Pipelines | `Pipeline` do scikit-learn | [`capitulo_13`](notebooks/capitulo_13_pipelines/capitulo_13.ipynb) |
| 14 | A Caça aos Hiperparâmetros | Grid Search e Random Search | [`capitulo_14`](notebooks/capitulo_14_a_caca_aos_hiperparametros/capitulo_14.ipynb) |
| 15 | Além da Acurácia | Matriz de confusão, precisão, recall, F1 | [`capitulo_15`](notebooks/capitulo_15_alem_da_acuracia/capitulo_15.ipynb) |
| 16 | O Threshold de Decisão | Ajuste de sensibilidade; curva ROC | [`capitulo_16`](notebooks/capitulo_16_o_threshold_de_decisao/capitulo_16.ipynb) |
| 17 | Classes Desbalanceadas | `class_weight`, SMOTE | [`capitulo_17`](notebooks/capitulo_17_classes_desbalanceadas/capitulo_17.ipynb) |
| 18 | Abrindo a Caixa-Preta | *Feature importance* e seus limites | [`capitulo_18`](notebooks/capitulo_18_abrindo_a_caixa_preta/capitulo_18.ipynb) |
| 19 | SHAP | Explicabilidade com valores de Shapley | [`capitulo_19`](notebooks/capitulo_19_shap/capitulo_19.ipynb) |
| 20 | LIME | Explicações locais por aproximação | [`capitulo_20`](notebooks/capitulo_20_lime/capitulo_20.ipynb) |
| 21 | Validação Cruzada Aninhada | O teste de estresse final do modelo | [`capitulo_21`](notebooks/capitulo_21_validacao_cruzada_aninhada/capitulo_21.ipynb) |
| 22 | Ensembles de Modelos | Voting / comitês de especialistas | [`capitulo_22`](notebooks/capitulo_22_ensembles_de_modelos/capitulo_22.ipynb) |
| 23 | Análise de Erros | Aprendendo com as falhas do modelo | [`capitulo_23`](notebooks/capitulo_23_analise_de_erros/capitulo_23.ipynb) |
| 24 | O Julgamento Final | Avaliação única no conjunto de teste reservado | [`capitulo_24`](notebooks/capitulo_24_o_julgamento_final/capitulo_24.ipynb) |
| 25 | Deployment | Do notebook a uma API em produção (FastAPI) | [`capitulo_25`](notebooks/capitulo_25_deployment/capitulo_25.ipynb) |
| 26 | Monitoramento | Detecção de *drift* e degradação em produção | [`capitulo_26`](notebooks/capitulo_26_monitoramento/capitulo_26.ipynb) |
| 27 | Fairness | Equidade entre subgrupos com `fairlearn` | [`capitulo_27`](notebooks/capitulo_27_fairness/capitulo_27.ipynb) |
| 28 | Explicabilidade Clínica | Da teoria à prática médica | [`capitulo_28`](notebooks/capitulo_28_explicabilidade_clinica/capitulo_28.ipynb) |
| 29 | A Carta de Helena — Uma Resposta | Encerramento narrativo (sem código) | — |
| 30 | Comparação de Modelos | Retrospectiva consolidada da jornada | [`capitulo_30`](notebooks/capitulo_30_comparacao_de_modelos/capitulo_30.ipynb) |
| 31 | Checklist Completo | Guia de campo para projetos de classificação (sem código) | — |
| 32 | Além do Binário | Multiclasse e reflexões finais (sem código) | — |

Os Capítulos 29, 31 e 32 são puramente narrativos ou de referência e não têm
notebook associado — seu conteúdo está apenas no livro.

## O projeto OncoClassify 2.0

- **Dataset**: Wisconsin Breast Cancer Dataset, versão didaticamente
  modificada (610 registros brutos → 600 amostras canônicas após curadoria,
  30 features morfológicas). Ver [`data/README.md`](data/README.md).
- **Convenção de rótulo fixa em todo o projeto**: `0 = Maligno`, `1 = Benigno`.
  A classe **Maligna é a classe positiva** de interesse clínico.
- **Custos assimétricos**: um falso negativo (câncer não detectado) custa
  10× mais que um falso positivo (`CUSTO_FN = 100`, `CUSTO_FP = 10`) —
  premissa que orienta a escolha de métrica e de *threshold* do Capítulo 3
  em diante.
- **Reprodutibilidade**: `RANDOM_STATE = 42` fixado em um único lugar
  (`src/oncoclassify_utils.py`) e herdado por todos os capítulos.
- **Modelo final**: ensemble de votação soft (Regressão Logística + SVM +
  Gradient Boosting), avaliado por validação cruzada aninhada e servido via
  FastAPI (`deploy/app.py`).

## Aviso legal

Este projeto é **material didático**. O dataset, os modelos e a API deste
repositório não constituem um dispositivo médico, não passaram por validação
clínica ou regulatória e não devem ser usados para apoiar diagnósticos reais.
Qualquer semelhança de resultados com casos reais é responsabilidade de quem
os reutilizar fora do contexto educacional em que foram criados.

## Como citar

```bibtex
@software{riz_de_barros_arquitetura_da_verdade,
  author  = {Riz de Barros, Alvaro},
  title   = {A Arquitetura da Verdade — A Saga da Classificação (código-fonte)},
  year    = {2026},
  url     = {https://github.com/profalvarobarros/Livro-A-Arquitetura-da-Verdade}
}
```

Ver também [`CITATION.cff`](CITATION.cff).

## Licença

- **Código** (notebooks, `src/`, `deploy/`, scripts e demais arquivos `.py`
  deste repositório): licenciado sob [MIT](LICENSE) — use, modifique e
  redistribua livremente, com atribuição.
- **Texto do livro**: *A Arquitetura da Verdade — A Saga da Classificação* ©
  2026 Alvaro Riz de Barros. Todos os direitos reservados. Este repositório
  não reproduz o texto integral da obra.
- **Dataset**: derivado do Wisconsin Breast Cancer Dataset (UCI Machine
  Learning Repository), de uso público para fins de pesquisa e ensino.

## Contribuindo

Correções de código, bugs em notebooks e sugestões de melhoria são bem-vindos
— ver [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Autor

**Alvaro Riz de Barros** — docente em Inteligência Artificial e Ciência de
Dados no IBMEC-RJ e professor de Análise Preditiva nos programas de MBA da
FGV. Graduado em Computação, com MBA em IA, Data Science e Big Data (PUC-RS),
MBA em Gestão de Marketing (IBMEC-RJ), Mestre em Engenharia de Sistemas
(UCP) e doutorando em Engenharia de Defesa (IME).

- E-mail: [alvaroriz@gmail.com](mailto:alvaroriz@gmail.com)
- LinkedIn, Lattes e ORCID: adicionar links aqui

---

*"Classificar não é apenas escolher a categoria certa. É entender o custo de
cada escolha errada, antes que alguém pague por ela no mundo real."*
