# Análise de Dados Climáticos com Python

Projeto educacional de análise de dados que integra coleta via API, processamento e visualização, com foco em transformar dados climáticos brutos em informações interpretáveis.

## Autor

Alex Sandro da Costa Silva Souza

## Visão Geral

Este projeto demonstra um fluxo completo de análise de dados:

1. Coleta de dados climáticos em tempo real e históricos via API
2. Tratamento e organização dos dados com Pandas
3. Geração de visualizações para análise exploratória
4. Representação geográfica com mapas interativos


## Tecnologias Utilizadas

- Python
- Requests (consumo de API)
- JSON (estrutura de dados)
- Pandas (tratamento e análise)
- Matplotlib (visualização)
- Folium (mapas interativos)

## Fonte dos Dados

Dados obtidos da API pública Open-Meteo:

- https://api.open-meteo.com/v1/forecast  
- https://archive-api.open-meteo.com/v1/archive  

A API fornece dados climáticos sem necessidade de autenticação, facilitando testes e experimentação.

## Estrutura do Projeto


PROJETO-CLIMA-PYTHON/
│
├── output/
│ ├── grafico_barras_temperatura.png
│ ├── grafico_dispersao_temperatura.png
│ ├── grafico_pizza_chuva.png
│ ├── mapa_calor_temperatura_media_anual.html
│ ├── mapa_calor_temperaturas.html
│ ├── temperatura_media_anual_cidades.csv
│
├── analise_clima.py
├── mapa_calor.py
├── mapa_calor_temperatura_anual.py
├── requirements.txt
├── .gitignore
└── README.md


## Funcionalidades

- Coleta de dados climáticos via API REST
- Normalização e estruturação de dados em DataFrame
- Análise exploratória básica
- Geração de visualizações:
  - Gráfico de barras (temperatura)
  - Gráfico de pizza (chuva)
  - Gráfico de dispersão (variação)
- Geração de mapas de calor interativos
- Exportação de dados para CSV

## Scripts

### analise_clima.py
Responsável pela coleta e análise de dados de previsão:

- Consome dados da API
- Processa e organiza informações
- Gera gráficos de análise

### mapa_calor.py
Responsável pela visualização geográfica atual:

- Coleta temperatura de múltiplas cidades
- Gera mapa de calor interativo

### mapa_calor_temperatura_anual.py
Responsável pela análise histórica:

- Coleta dados históricos
- Calcula média anual por cidade
- Exporta dados estruturados
- Gera mapa de calor anual

## Como Executar

### 1. Clonar o repositório


git clone https://github.com/AledSouza/projeto-clima-python.git
cd PROJETO-CLIMA-PYTHON


### 2. Instalar dependências


pip install -r requirements.txt


### 3. Executar os scripts


python analise_clima.py
python mapa_calor.py
python mapa_calor_temperatura_anual.py


## Resultados Gerados

Os resultados são armazenados na pasta `output/` e incluem:

- Visualizações em formato PNG
- Mapas interativos em HTML
- Dataset processado em CSV

## Considerações

O projeto foi estruturado com foco didático, mas segue práticas utilizadas em projetos reais de análise de dados, como separação de responsabilidades, organização de outputs e uso de bibliotecas consolidadas.

## Conclusão

Este projeto consolida conceitos essenciais de análise de dados, integrando coleta, processamento e visualização, servindo como base para aplicações mais avançadas na área.