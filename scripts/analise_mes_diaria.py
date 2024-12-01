import pandas as pd
import matplotlib.pyplot as plt

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

base_dados['mes_entrada'] = pd.to_datetime(base_dados['data_chegada']).dt.month

base_dados['total_noites'] = base_dados['nro_noites_fds'] + base_dados['nro_noites_dds']

agrupamento_fds_dds = base_dados.groupby('mes_entrada')[['nro_noites_fds', 'nro_noites_dds']].sum()

agrupamento_fds_dds.to_csv('./csv/analise_mensal_noites.csv')

plt.figure(figsize=(12, 6))
plt.bar(agrupamento_fds_dds.index, agrupamento_fds_dds['nro_noites_fds'], color='skyblue', label='Finais de Semana')
plt.bar(agrupamento_fds_dds.index, agrupamento_fds_dds['nro_noites_dds'], 
        bottom=agrupamento_fds_dds['nro_noites_fds'], color='salmon', label='Dias de Semana')
plt.title('Distribuição de Diárias por Mês (FDS vs. DDS)')
plt.xlabel('Mês')
plt.ylabel('Número de Diárias')
plt.xticks(ticks=range(1, 13), labels=[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('./visualizacoes/grafico_diarias_por_mes.png')

