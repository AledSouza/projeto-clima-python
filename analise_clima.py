import requests
import pandas as pd
import matplotlib.pyplot as plt


url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=-22.9068"
    "&longitude=-43.1729"
    "&hourly=temperature_2m,relative_humidity_2m,precipitation"
    "&forecast_days=7"
)

#Requisição e checagem de erro
resposta = requests.get(url)

if resposta.status_code == 200:
    print("dados acessados com sucesso!")
    print(resposta)

else:
    print("Erro ao acessar a API:", resposta.status_code)
    exit()

dados_json = resposta.json()

print("\n Chaves principais do JSON:")
print(dados_json.keys())
