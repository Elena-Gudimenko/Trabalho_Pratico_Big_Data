import pandas as pd

pd.set_option('display.max_rows', 9999)

# ---------------------------------------------------------------
# Steps 3 and 4: read the CSV and store it in a variable
# ---------------------------------------------------------------
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# ---------------------------------------------------------------
# Step 5: check that the data was imported correctly
# ---------------------------------------------------------------
print('===== Passo 5a: informacoes gerais =====')
dados.info()

print('\n===== Passo 5b: primeiras 5 linhas =====')
print(dados.head(5))
print('\n===== Passo 5b: ultimas 5 linhas =====')
print(dados.tail(5))

# ---------------------------------------------------------------
# Step 6: work on a copy, keep the original untouched
# ---------------------------------------------------------------
dados_tratados = dados.copy()

# ---------------------------------------------------------------
# Step 7: replace null values in 'Calories' with 0
# ---------------------------------------------------------------
dados_tratados['Calories'] = dados_tratados['Calories'].fillna(0)

print('\n===== Passo 7b: Calories sem nulos (linhas 18 e 28 = 0) =====')
print(dados_tratados.to_string())

# ---------------------------------------------------------------
# Step 8: replace null values in 'Date' with '1900/01/01'
# ---------------------------------------------------------------
dados_tratados['Date'] = dados_tratados['Date'].fillna('1900/01/01')

print('\n===== Passo 8b: Date sem nulos (linha 22 = 1900/01/01) =====')
print(dados_tratados.to_string())

# Step 8c: try to convert 'Date' to datetime.
# Expected to fail: pandas infers the format "'%Y/%m/%d'" (with quotes)
# from the first rows, and '1900/01/01' has no quotes.
print('\n===== Passo 8c: tentativa de to_datetime =====')
try:
    dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'])
except ValueError as erro:
    print('Erro esperado:', erro)

# ---------------------------------------------------------------
# Step 9: replace '1900/01/01' with NaN and try again
# ---------------------------------------------------------------
dados_tratados['Date'] = dados_tratados['Date'].replace('1900/01/01', float('nan'))

print('\n===== Passo 9b: nova tentativa de to_datetime =====')
try:
    dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'])
except ValueError as erro:
    # Expected to fail again, now because of the value 20201226 (row 26)
    print('Erro esperado:', erro)

print('\n===== Passo 9c: conjunto apos substituir 1900/01/01 por NaN =====')
print(dados_tratados.to_string())

# ---------------------------------------------------------------
# Step 10: fix the value 20201226 using replace + to_datetime
# ---------------------------------------------------------------
# to_datetime parses '20201226'; strftime writes it back in the same
# format as the other rows ('YYYY/MM/DD' with quotes)
data_corrigida = pd.to_datetime('20201226', format='%Y%m%d').strftime("'%Y/%m/%d'")
dados_tratados['Date'] = dados_tratados['Date'].replace('20201226', data_corrigida)

# ---------------------------------------------------------------
# Step 11: convert the whole 'Date' column to datetime
# ---------------------------------------------------------------
dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format="'%Y/%m/%d'")

print('\n===== Passo 11: Date convertida para datetime =====')
print(dados_tratados.to_string())
print('\nTipo da coluna Date:', dados_tratados['Date'].dtype)

# ---------------------------------------------------------------
# Step 12: remove records with null values (only row 22, column 'Date')
# ---------------------------------------------------------------
dados_tratados = dados_tratados.dropna(subset=['Date'])

# ---------------------------------------------------------------
# Step 13: final check
# ---------------------------------------------------------------
print('\n===== Passo 13: conjunto de dados final =====')
print(dados_tratados.to_string())
print()
dados_tratados.info()
