# Análise de Dados do Resort

Este projeto é uma análise exploratória e descritiva de dados de um resort fictício, focando em descobrir padrões, comportamentos de clientes e identificar oportunidades para aumento de receita. A análise foi realizada utilizando Python e bibliotecas específicas para manipulação e visualização de dados.

## Objetivos

### Entender o comportamento dos clientes:
- Identificar segmentos com maiores taxas de cancelamento.
- Avaliar a composição dos hóspedes: famílias, clientes corporativos, etc.
- Analisar o impacto da antecedência da reserva nos cancelamentos.

### Otimizar a ocupação e receita:
- Comparar o uso de finais de semana (FDS) e dias de semana (DDS).
- Explorar estratégias para atrair famílias e outros segmentos.

### Propor melhorias estratégicas:
- Estratégias para reduzir cancelamentos.
- Incentivos para reservas em períodos de baixa ocupação.

## Árvore de Hipóteses

### Segmentação de Clientes:
- Clientes Corporativos cancelam menos devido à necessidade de viagens a trabalho.
- Famílias (com crianças ou bebês) reservam com maior antecedência e apresentam maior probabilidade de cancelamento.

### Tempo de Permanência:
- Famílias tendem a permanecer mais nos finais de semana.
- Ocupação em dias úteis é predominantemente de clientes individuais e corporativos.

### Mercado Nacional x Internacional:
- Clientes internacionais reservam mais frequentemente por agências online.
- Clientes brasileiros reservam diretamente ou por agências offline.

### Impacto de Antecedência:
- Reservas feitas com alta antecedência apresentam maiores taxas de cancelamento.

### Taxas de Cancelamento por Segmento:
- Grupos organizados têm menores taxas de cancelamento devido à logística envolvida.
- Famílias e indivíduos apresentam maiores taxas de cancelamento.

## Análises Realizadas

1. **Taxas de Cancelamento**
   - Analisamos os segmentos de mercado para identificar aqueles com maior propensão a cancelar reservas.
   - **Resultado:** Clientes individuais e famílias apresentaram maior taxa de cancelamento.

2. **Análise por Mercado**
   - Comparação entre mercado nacional (Brasil) e internacional.
   - **Resultado:** A maioria das reservas são internacionais, com uma parcela significativa de clientes com país de origem desconhecido.

3. **Famílias**
   - Segmentamos as famílias em três grupos:
     - Com crianças.
     - Com bebês.
     - Com ambos.
   - **Resultado:** Famílias com crianças e bebês apresentam maior permanência média.

4. **Tempo de Permanência**
   - Analisamos as noites em finais de semana (FDS) e dias de semana (DDS).
   - **Resultado:** A maioria das famílias prefere FDS, enquanto outros segmentos ocupam mais os dias úteis.

5. **Principais Agências**
   - Identificamos as agências que mais encaminham hóspedes.
   - **Resultado:** A maior parte das reservas veio de agências online.

## Estrutura do Projeto

```bash
├── data/ # Dados utilizados para as análises 
│ ├── base_dados_processada.pkl 
│ └── base_dados_original.csv 
├── visualizacoes/ # Gráficos gerados 
│ ├── grafico_cancelamentos.png 
│ ├── grafico_diarias_por_mes.png 
│ ├── grafico_familias.png 
│ └── grafico_agencias_top10.png 
├── csv/ # Relatórios gerados 
│ ├── analise_mensal_noites.csv 
│ ├── valores_mercado.csv 
│ └── cancelamentos_por_segmento.csv 
├── scripts/ # Scripts de análise 
│ ├── analise_cancelamentos.py 
│ ├── analise_familias.py 
│ ├── analise_mercado.py 
│ ├── analise_segmentos.py 
│ └── analise_diarias.py 
├── README.md # Documentação do projeto 
└── requirements.txt # Dependências do projeto
```


## Bibliotecas Utilizadas
- **Pandas:** Manipulação e análise de dados tabulares.
- **Matplotlib:** Criação de gráficos básicos.
- **Seaborn:** Visualizações estatísticas mais avançadas.

## Instalação

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/analise-dados-resort.git
cd analise-dados-resort
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Certifique-se de que os dados estão na pasta data/.

## Como executar

Certifique-se de que o arquivo base_dados_processada.pkl está localizado no diretório /data/.

Execute o script principal main.py diretamente no terminal:

```bash
python main.py
```

Os resultados da análise serão gerados automaticamente:

Arquivos .csv salvos no diretório /csv/.
Gráficos salvos no diretório /visualizacoes/.
Logs e mensagens importantes serão exibidos no terminal durante a execução.

## Resultados
Os resultados incluem gráficos, tabelas e insights que podem ser utilizados para:

- Reduzir cancelamentos.
- Aumentar a ocupação em períodos ociosos.
- Otimizar a estratégia de marketing e relacionamento com os clientes.



