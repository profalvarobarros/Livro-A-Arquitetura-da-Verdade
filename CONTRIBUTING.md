# Contribuindo

Obrigado pelo interesse em melhorar este repositório. Ele acompanha um livro
publicado, então o escopo de contribuições é intencionalmente restrito ao
**código**: notebooks, `src/`, `deploy/` e infraestrutura do repositório. O
texto do livro em si não é gerenciado aqui.

## Como reportar um problema

Abra uma *issue* descrevendo:

1. Capítulo e notebook afetados (ex.: `notebooks/capitulo_17_classes_desbalanceadas`).
2. Comportamento esperado vs. observado, com o erro completo se houver.
3. Ambiente: versão do Python e se você usou `requirements.txt` sem alterações.

Erros que quebram a reprodutibilidade dos números citados no livro (métricas,
formas de dataset, seeds) têm prioridade alta — por favor sinalize isso no
título da issue.

## Como propor uma correção

1. Faça um fork e crie uma branch descritiva (`fix/capitulo-14-grid-search`).
2. Se a mudança altera qualquer número reportado no livro (acurácia, recall,
   shape de dataset etc.), rode o notebook do início ao fim e confirme que os
   resultados continuam batendo com o texto — ou explique na PR por que
   mudaram.
3. Mantenha o estilo existente: comentários em português, `random_state=42`
   fixado via `src/utils.py` / `src/oncoclassify_utils.py`, sem introduzir
   dependências fora de `requirements.txt` sem justificativa.
4. Abra o Pull Request explicando o problema original e a correção.

## O que não é aceito aqui

- Alterações ao texto narrativo do livro (esse conteúdo não está neste
  repositório — ver README).
- Reescrituras de estilo sem correção funcional associada.
- Novas dependências pesadas para ganhos marginais.

## Dúvidas

Para questões gerais sobre o livro ou a trilogia "A Carta dos Modelos",
use os contatos listados no README principal.
