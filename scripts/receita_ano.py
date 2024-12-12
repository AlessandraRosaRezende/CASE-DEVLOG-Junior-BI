# receita por ano
import pandas as pd
import matplotlib.pyplot as plt

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

receita_por_ano = base_dados.groupby('ano_chegada')['receita_por_noite'].mean()

receita_por_ano.to_csv('./csv/receita_por_ano.csv', header=True)

plt.figure(figsize=(10, 6))
receita_por_ano.plot(kind='bar', color='coral')
plt.title('Receita Média por Ano de Chegada')
plt.xlabel('Ano de Chegada')
plt.ylabel('Receita por Noite')
plt.xticks(rotation=45)
plt.savefig('./visualizacoes/receita_por_ano.png')
