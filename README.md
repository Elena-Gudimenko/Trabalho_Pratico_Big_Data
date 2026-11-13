# Trabalho Prático – DGT2823 Tecnologias para desenv. de soluções de big data

Limpeza de um conjunto de dados com Python e a biblioteca Pandas.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `dados.csv` | Conjunto de dados fornecido (separador `;`) |
| `microatividades.py` | Microatividades 1 a 5 (leitura, subconjunto, `max_rows`, `head`/`tail`, `info`) |
| `trabalho_pratico.py` | Trabalho prático: tratamento dos dados (passos 1 a 13) |

## Como executar

```bash
pip install pandas
python microatividades.py
python trabalho_pratico.py
```

## Tratamentos realizados

1. Valores nulos de `Calories` (linhas 18 e 28) substituídos por `0`.
2. Valor nulo de `Date` (linha 22) substituído por `1900/01/01` e, após o erro de formato, por `NaN`.
3. Valor `20201226` (linha 26) convertido com `replace` + `to_datetime` para o mesmo formato das demais datas.
4. Coluna `Date` convertida para `datetime`.
5. Registro com data nula (linha 22) removido com `dropna`.
