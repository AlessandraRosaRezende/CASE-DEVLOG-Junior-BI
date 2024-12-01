import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

receita_por_quarto = base_dados.groupby('tipo_quarto')['receita_por_noite'].mean()

receita_por_quarto.to_csv('./csv/receita_por_quarto.csv', header=True)

plt.figure(figsize=(10, 6))
sns.barplot(x=receita_por_quarto.index, y=receita_por_quarto.values)
plt.title('Receita Média por Tipo de Quarto')
plt.xlabel('Tipo de Quarto')
plt.ylabel('Receita Média por Noite')
plt.xticks(rotation=45)
plt.savefig('./visualizacoes/receita_media_por_quarto.png')

