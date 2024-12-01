import pandas as pd
import matplotlib.pyplot as plt

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

cancelamentos_por_segmento = base_dados.groupby('segmento_mercado')['reserva_cancelada'].mean() * 100 

print("Porcentagem de cancelamentos por segmento de mercado:")
print(cancelamentos_por_segmento)

cancelamentos_por_segmento.to_csv('./csv/cancelamentos_por_segmento.csv', header=True)

plt.figure(figsize=(10, 6))
cancelamentos_por_segmento.plot(kind='bar', color='skyblue')
plt.title('Porcentagem de Cancelamentos por Segmento de Mercado')
plt.xlabel('Segmento de Mercado')
plt.ylabel('Porcentagem de Cancelamentos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./visualizacoes/grafico_cancelamentos_por_segmento.png')

