import pandas as pd

# Sempre abrir um arquivo de dados.

# XLS (Excel) pd.read_excel
# CSV/TXT pd.read_csv
# Dicionário pd.Dataframe

dataframe = pd.read_csv("dadostxt.txt", sep=",")
print(dataframe.head())