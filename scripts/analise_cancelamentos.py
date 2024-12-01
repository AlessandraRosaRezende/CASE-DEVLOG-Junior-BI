import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

cancelamentos = base_dados[base_dados['reserva_cancelada'] == 1]

num_cancelamentos = cancelamentos.shape[0]
print(f"Total de reservas canceladas: {num_cancelamentos}")

num_cancelamentos_df = pd.DataFrame({'Total Cancelamentos': [num_cancelamentos]})

num_cancelamentos_df.to_csv('./csv/num_cancelamentos.csv', index=False)

plt.figure(figsize=(8, 5))
sns.countplot(x='reserva_cancelada', data=base_dados)
plt.title('Análise de Cancelamentos de Reservas')
plt.xlabel('Cancelada')
plt.ylabel('Número de Reservas')
plt.xticks([0, 1], ['Não', 'Sim'])
plt.savefig('./visualizacoes/grafico_cancelamentos.png')


