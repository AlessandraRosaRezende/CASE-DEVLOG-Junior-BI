import pandas as pd
import matplotlib.pyplot as plt

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

base_dados['país'].fillna('Desconhecido', inplace=True)

mercado_substituido = base_dados['país'].value_counts()

mercado_nacional = mercado_substituido['BRA'] if 'BRA' in mercado_substituido else 0

mercado_desconhecido = mercado_substituido['Desconhecido'] if 'Desconhecido' in mercado_substituido else 0

mercado_internacional = mercado_substituido.sum() - mercado_nacional - mercado_desconhecido

print(f"Reservas nacionais (Brasil): {mercado_nacional}")
print(f"Reservas internacionais: {mercado_internacional}")
print(f"Reservas com país desconhecido: {mercado_desconhecido}")

dados_mercado = ['Nacional (Brasil)', 'Internacional', 'Desconhecido']
valores_mercado = [mercado_nacional, mercado_internacional, mercado_desconhecido]

df_mercado = pd.DataFrame({
    'Segmento': dados_mercado,
    'Reservas': valores_mercado
})

df_mercado.to_csv('./csv/valores_mercado.csv', index=False)

plt.figure(figsize=(8, 8))
plt.pie(valores_mercado, labels=dados_mercado, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgray'])
plt.title('Distribuição de Mercado (Nacional, Internacional e Desconhecido)')
plt.savefig('./visualizacoes/grafico_mercado.png')

