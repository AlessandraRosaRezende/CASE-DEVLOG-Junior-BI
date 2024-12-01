import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

base_dados_clean = base_dados[base_dados['agencia_turismo'].notnull() & (base_dados['agencia_turismo'] != 0)]

base_dados_clean['total_hospedes'] = base_dados_clean['adultos'] + base_dados_clean['criancas'] + base_dados_clean['bebes']

hospedes_por_agencia = base_dados_clean.groupby('agencia_turismo')['total_hospedes'].sum()

top_10_agencias = hospedes_por_agencia.sort_values(ascending=False).head(10)

print("Top 10 Agências que mais trouxeram hóspedes:")
print(top_10_agencias)

top_10_agencias.to_csv('./csv/top_10_agencias.csv', header=True)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_agencias.index, y=top_10_agencias.values, palette='viridis')
plt.title('Top 10 Agências que mais trouxeram Hóspedes')
plt.xlabel('Agência de Turismo')
plt.ylabel('Número de Hóspedes')
plt.xticks(rotation=45, ha='right')
plt.savefig('./visualizacoes/top_10_agencias_hospedes.png')

