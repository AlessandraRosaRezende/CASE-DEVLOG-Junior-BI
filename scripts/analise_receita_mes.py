import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

base_dados['mes_chegada'] = base_dados['mes_chegada'].astype(int) 
receita_por_mes = base_dados.groupby('mes_chegada')['receita_por_noite'].mean()

receita_por_mes.to_csv('./csv/receita_por_mes.csv', header=True)

plt.figure(figsize=(10, 6))
receita_por_mes.plot(kind='line', marker='o', color='green')
plt.title('Receita Média por Mês de Chegada')
plt.xlabel('Mês de Chegada')
plt.ylabel('Receita por Noite')
plt.xticks(range(1, 13)) 
plt.savefig('./visualizacoes/receita_por_mes.png') 

