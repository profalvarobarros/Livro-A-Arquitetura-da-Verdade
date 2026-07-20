# Dados

## `WisconsinBreastCancerDataset_MODIFIED.csv`

Versão didaticamente modificada do **Wisconsin Breast Cancer Dataset**
(Wolberg et al., UCI Machine Learning Repository, 1992).

O dataset original tem 569 amostras e 30 features morfológicas, extraídas de
imagens digitalizadas de uma Aspiração por Agulha Fina (AAF) de massas
mamárias. Para este livro, ele foi deliberadamente modificado para 610
registros, com problemas injetados de propósito — duplicatas, valores
ausentes, colunas de identificação, colunas clínicas fracas e duas colunas
de **vazamento de alvo** (*data leakage*) — para servir de exercício de
curadoria (Capítulo 1) e detecção de vazamento (Capítulo 4).

Após a curadoria descrita no Capítulo 1, chega-se à **base canônica de
modelagem**: 600 amostras × 30 features morfológicas (380 casos benignos,
220 malignos). É sobre essa base que o restante do livro — e a maior parte
dos notebooks deste repositório — trabalha, via `src/oncoclassify_utils.py`.

Convenção de rótulo fixa em todo o projeto: `0 = Maligno`, `1 = Benigno`.

## Aviso

Este dataset e os modelos treinados a partir dele têm **finalidade
exclusivamente educacional**. Não são um dispositivo médico, não foram
validados clinicamente e não devem ser usados, direta ou indiretamente,
para apoiar decisões diagnósticas reais. Ver aviso completo no README
principal do repositório.

## Proveniência

- Dataset original: [UCI Machine Learning Repository — Breast Cancer
  Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)
- Contexto médico completo (procedimento AAF, significado de cada feature):
  Apêndice B do livro.
