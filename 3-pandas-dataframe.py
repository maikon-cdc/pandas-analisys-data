# ================================
# Exemplo com Pandas DataFrame
# ================================

# Pandas é uma biblioteca de análise de dados em Python.
# A estrutura principal do Pandas é o DataFrame, que funciona como uma "tabela":
#   - linhas (indexadas automaticamente, começando de 0)
#   - colunas (nomeadas)
# Cada coluna pode ter um tipo de dado (int, float, string etc).
# Muito usado em ciência de dados, análise de planilhas, BI e machine learning.

import pandas as pd

print("===== PANDAS DATAFRAME =====")

# Criando um DataFrame manualmente (passando um dicionário)
# A chave do dicionário vira o nome da coluna
# A lista associada à chave vira os valores daquela coluna
df = pd.DataFrame({
    "Nome": ["Ana", "João", "Maria"],   # Coluna de strings
    "Idade": [25, 30, 28],              # Coluna de inteiros
    "Salário": [3500, 4200, 5000]       # Coluna de floats/inteiros
})

print(df)  # Mostra a tabela formatada


# ===== ACESSANDO COLUNAS =====
# Podemos acessar uma coluna pelo seu nome, como se fosse um dicionário
print("\nColuna Idade:")
print(df["Idade"])  # Retorna uma Series (estrutura de coluna do Pandas)


# ===== FILTRANDO LINHAS =====
# Podemos aplicar condições para filtrar os dados.
# Exemplo: mostrar apenas quem tem salário maior que 4000
print("\nQuem tem salário > 4000:")
print(df[df["Salário"] > 4000])  
# Retorna um novo DataFrame apenas com linhas que satisfazem a condição


# ===== CRIANDO DATAFRAME DE OUTRA FORMA =====
# Também podemos criar DataFrame a partir de uma lista de listas,
# e especificar os nomes das colunas manualmente.
dados = [
    ["Pedro", 22, 3100],
    ["Carla", 27, 4700]
]
df2 = pd.DataFrame(dados, columns=["Nome", "Idade", "Salário"])
print("\nOutro DataFrame:")
print(df2)


# ===== CONCATENANDO DATAFRAMES =====
# Podemos unir (concatenar) vários DataFrames em um só.
# Aqui, juntamos df e df2 (um abaixo do outro).
df_total = pd.concat([df, df2])
print("\nDataFrame combinado:")
print(df_total)