import pandas as pd
import matplotlib.pyplot as plt

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

receita_por_segmento = base_dados.groupby('segmento_mercado')['receita_por_noite'].mean()

receita_por_segmento.to_csv('./csv/receita_por_segmento.csv', header=True)

plt.figure(figsize=(10, 6))
receita_por_segmento.plot(kind='bar', color='coral')
plt.title('Receita Média por Segmento de Mercado')
plt.xlabel('Segmento de Mercado')
plt.ylabel('Receita por Noite')
plt.xticks(rotation=45)
plt.savefig('./visualizacoes/receita_por_segmento.png') 

print(receita_por_segmento)
