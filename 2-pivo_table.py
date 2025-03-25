import pandas as pd

data = pd.read_excel("data/VendaCarros.xlsx")
nome='Thaigo'
print(type(data))

#2- Selecionando colunas especificas do dataframe
df=data [["Fabricante","ValorVenda","Ano"]]
print(df)

#3 - Criando tabela pivo
pivot_table = df.pivot_table(values='ValorVenda', index='Ano', aggfunc='sum',columns='Fabricante')

print(pivot_table)

#4- Exportar tabela pivo em arquivo excel
pivot_table . to_excel ("data/pivot_table.xlsx","Relatorio") 