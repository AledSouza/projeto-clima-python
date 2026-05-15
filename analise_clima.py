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