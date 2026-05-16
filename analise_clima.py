import requests
import pandas as pd
import matplotlib.pyplot as plt
import os


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

dados_horarios = dados_json["hourly"]
df = pd.DataFrame(dados_horarios)
# print(df)

print("\n Primeiras linhas do Dataframe:")
# print(df.head())

df["time"] = pd.to_datetime(df["time"])
df["data"] = df["time"].dt.date

print("\nResumo estatítico")
print(df.describe())

#Acumulo diario utilizando groupby

df_diario = df.groupby("data").agg({
    "temperature_2m" : "mean",
    "relative_humidity_2m": "mean",
    "precipitation" : "sum"
}).reset_index()

print("\n Dados agrupados por dia:")
print(df_diario)

#temperatura média por dia

plt.figure(figsize=(10,5))
plt.bar(df_diario["data"].astype(str), df_diario["temperature_2m"])
plt.title("Temperatura Média por dia - Rio de Janeiro")
plt.xlabel("Data")
plt.ylabel(("Temperatura média (°C)"))
plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
os.makedirs("output", exist_ok=True)
plt.savefig("output/grafico_barras_temperatura.png")
plt.show()

#gráfico de pizza

plt.figure(figsize=(7,7))
plt.pie(
    df_diario["precipitation"],
    labels=df_diario["data"].astype(str),
    autopct="%1.1f%%"
    
    
)
plt.title("Distribuição da precipitação diaria:")
plt.tight_layout()
plt.savefig("output/grafico_pizza_chuva.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["temperature_2m"], df["relative_humidity_2m"])
plt.title("Relação entre temperatura e umidade")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Umidade relativa (%)")
plt.tight_layout()
plt.savefig("output/grafico_dispersao_temperatura_umidade.png")
plt.show()

