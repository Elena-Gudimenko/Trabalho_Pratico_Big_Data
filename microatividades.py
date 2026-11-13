import pandas as pd

# ---------------------------------------------------------------
# Microatividade 1: read a CSV file with Pandas
# ---------------------------------------------------------------
# sep: column separator; engine: 'python' parser; encoding: file charset
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

print('===== Microatividade 1: dados lidos do CSV =====')
print(dados)

# ---------------------------------------------------------------
# Microatividade 2: create a subset with only 3 columns
# ---------------------------------------------------------------
subconjunto = dados[['Duration', 'Pulse', 'Calories']]

print('\n===== Microatividade 2: subconjunto (3 colunas) =====')
print(subconjunto)

# ---------------------------------------------------------------
# Microatividade 3: set max_rows and print the whole dataset
# ---------------------------------------------------------------
pd.set_option('display.max_rows', 9999)

print('\n===== Microatividade 3: conjunto completo com to_string() =====')
print(dados.to_string())

# ---------------------------------------------------------------
# Microatividade 4: first and last 10 rows
# ---------------------------------------------------------------
print('\n===== Microatividade 4: primeiras 10 linhas =====')
print(dados.head(10))

print('\n===== Microatividade 4: ultimas 10 linhas =====')
print(dados.tail(10))

# ---------------------------------------------------------------
# Microatividade 5: general information about the dataset
# ---------------------------------------------------------------
print('\n===== Microatividade 5: informacoes gerais =====')
# info() shows: number of rows (RangeIndex), number of columns,
# non-null count per column, dtype of each column and memory usage
dados.info()

# The same answers, extracted explicitly
print('\nTotal de linhas:', dados.shape[0])
print('Total de colunas:', dados.shape[1])
print('Quantidade de dados nulos por coluna:')
print(dados.isnull().sum())
print('Tipo de dado de cada coluna:')
print(dados.dtypes)
print('Memoria utilizada (bytes):', dados.memory_usage(deep=True).sum())
