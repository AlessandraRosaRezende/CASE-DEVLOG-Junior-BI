import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dados = pd.read_pickle("./data/base_dados_processada.pkl")

def categorizar_tipo_familia(row):
    if row['criancas'] > 0 and row['bebes'] > 0:
        return 'Ambos (Criança e Bebê)'
    elif row['criancas'] > 0:
        return 'Somente Criança'
    elif row['bebes'] > 0:
        return 'Somente Bebê'
    else:
        return 'Nao Categoria Familia' 

base_dados['tipo_familia'] = base_dados.apply(categorizar_tipo_familia, axis=1)

familias = base_dados[base_dados['tipo_familia'] != 'Nao Categoria Familia']

familia_counts = familias['tipo_familia'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(familia_counts, labels=familia_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(familia_counts)))
plt.title('Distribuição de Tipos de Famílias')
plt.axis('equal')  
plt.savefig('./visualizacoes/grafico_pizza_tipo_familias.png')

tempo_permanencia_fds = familias.groupby('tipo_familia')['nro_noites_fds'].sum()
tempo_permanencia_dds = familias.groupby('tipo_familia')['nro_noites_dds'].sum()

tempo_permanencia_fds.to_csv('./csv/tempo_permanencia_fds.csv', header=True)
tempo_permanencia_dds.to_csv('./csv/tempo_permanencia_dds.csv', header=True)

plt.figure(figsize=(8, 8))
plt.pie(tempo_permanencia_fds, labels=tempo_permanencia_fds.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(tempo_permanencia_fds)))
plt.title('Distribuição de Tempo de Permanência nos Finais de Semana por Tipo de Família')
plt.axis('equal')  
plt.savefig('./visualizacoes/grafico_pizza_tempo_permanencia_fds_familias.png')

plt.figure(figsize=(8, 8))
plt.pie(tempo_permanencia_dds, labels=tempo_permanencia_dds.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(tempo_permanencia_dds)))
plt.title('Distribuição de Tempo de Permanência Durante a Semana por Tipo de Família')
plt.axis('equal')
plt.savefig('./visualizacoes/grafico_pizza_tempo_permanencia_dds_familias.png')

