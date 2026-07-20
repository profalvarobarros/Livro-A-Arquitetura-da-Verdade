# Modelos

## `oncoclassify_v2.pkl`

Artefato de produção do projeto **OncoClassify 2.0**: um `VotingClassifier`
(votação soft) combinando Regressão Logística, SVM (kernel RBF) e Gradient
Boosting, treinado nas 600 amostras da base canônica após a validação final
do Capítulo 24 ("O Julgamento Final").

Gerado por `deploy/treinar_modelo.py` e consumido por `deploy/app.py`. Para
regenerá-lo do zero:

```bash
python deploy/treinar_modelo.py
```

Uso exclusivamente educacional — ver aviso legal no README principal.
