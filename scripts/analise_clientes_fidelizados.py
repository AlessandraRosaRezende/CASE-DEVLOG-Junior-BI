import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

clientes_fidelizados = base_dados.groupby('cliente_recorrente').size()
clientes_fidelizados = clientes_fidelizados[clientes_fidelizados > 2]

num_fidelizados = clientes_fidelizados.shape[0]
print(f"Total de clientes fidelizados (mais de 2 reservas): {num_fidelizados}")

num_fidelizados = pd.DataFrame({'Total Fidelizados': [num_fidelizados]})

num_fidelizados.to_csv('./csv/num_fidelizados.csv', index=False)

plt.figure(figsize=(8, 5))
sns.countplot(x='cliente_recorrente', data=base_dados)
plt.title('Fidelização de Clientes')
plt.xlabel('Cliente Recorrente')
plt.ylabel('Número de Reservas')
plt.xticks([0, 1], ['Não', 'Sim'])
plt.savefig('./visualizacoes/grafico_fidelizacao.png')

