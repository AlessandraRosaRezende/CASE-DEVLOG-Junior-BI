import pandas as pd
import os

file_path = "./data/CaseResort.xlsx" 

planilha = pd.ExcelFile(file_path)

print("Abas disponíveis na planilha:")
print(planilha.sheet_names)

base_dados = pd.read_excel(file_path, sheet_name="Base de Dados")

print("Primeiras linhas da Base de Dados:")
print(base_dados.head())

print("\nInformações sobre a Base de Dados:")
print(base_dados.info())

print("\nResumo estatístico:")
print(base_dados.describe())

print("\nValores ausentes por coluna:")
print(base_dados.isnull().sum())

base_dados.to_pickle("./data/base_dados_processada.pkl")

scripts_path = "./scripts"

scripts = [f for f in os.listdir(scripts_path) if f.endswith('.py')]

for script in scripts:
    script_path = os.path.join(scripts_path, script)
    with open(script_path) as file:
        exec(file.read())
    print(f"Executado: {script}")

print("Todos os scripts foram executados com sucesso.")
