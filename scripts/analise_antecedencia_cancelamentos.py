import pandas as pd
import matplotlib.pyplot as plt

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

print(base_dados.columns)

bins = [0, 7, 14, 30, 60, 90, float('inf')]
labels = ['0-7 dias', '8-14 dias', '15-30 dias', '31-60 dias', '61-90 dias', '91+ dias']
base_dados['intervalo_antecedencia'] = pd.cut(base_dados['tempo_antecedencia'], bins=bins, labels=labels)

cancelamentos_por_intervalo = base_dados.groupby('intervalo_antecedencia')['reserva_cancelada'].mean() * 100

print("Porcentagem de cancelamentos por intervalo de antecedência:")
print(cancelamentos_por_intervalo)

cancelamentos_por_intervalo.to_csv('./csv/cancelamentos_por_intervalo.csv', header=True)

plt.figure(figsize=(8, 8))
plt.pie(cancelamentos_por_intervalo, labels=cancelamentos_por_intervalo.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Porcentagem de Cancelamentos por Tempo de Antecedência')
plt.axis('equal')  
plt.savefig('./visualizacoes/grafico_pizza_cancelamentos_antecedencia.png')

plt.figure(figsize=(10, 6))
cancelamentos_por_intervalo.plot(kind='bar', color=plt.cm.Paired.colors)
plt.title('Porcentagem de Cancelamentos por Tempo de Antecedência')
plt.xlabel('Intervalo de Antecedência (dias)')
plt.ylabel('Porcentagem de Cancelamentos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./visualizacoes/grafico_barras_cancelamentos_antecedencia.png')

