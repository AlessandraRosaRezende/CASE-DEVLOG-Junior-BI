import pandas as pd
import matplotlib.pyplot as plt

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

# num reservas = nro_noites_dds+nro_noites_fds
base_dados['nro_noites_dds'] = base_dados['nro_noites_dds'].fillna(0)
base_dados['nro_noites_fds'] = base_dados['nro_noites_fds'].fillna(0)
base_dados['nro_reservas'] = base_dados['nro_noites_dds'] + base_dados['nro_noites_fds']

# agrupar por segmento de mercado
reservas_por_segmento = base_dados.groupby('segmento_mercado')['nro_reservas'].sum()

reservas_por_segmento.to_csv('./csv/reservas_por_segmento.csv', header=True)

plt.figure(figsize=(10, 6))
reservas_por_segmento.plot(kind='bar', color='coral')
plt.title('Número de Reservas por Segmento de Mercado')
plt.xlabel('Segmento de Mercado')
plt.ylabel('Número de Reservas')
plt.xticks(rotation=45)
plt.savefig('./visualizacoes/reservas_por_segmento.png')
