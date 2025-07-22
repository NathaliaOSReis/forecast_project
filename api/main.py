from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Consulta a previsão do tempo básica (temperatura & chuva) para a latitude/longitude fornecidas.")

OPENMETEO_URL = "https://api.open-meteo.com/v1/forecast"

class ForecastRequest(BaseModel):
    latitude: float
    longitude: float

@app.get("/")
def home():
    return {"mensagem": "🌦️ API de Clima rodando com Open-Meteo!"}

@app.post("/forecast")
def get_forecast(req: ForecastRequest):
    params = {
        "latitude": req.latitude,
        "longitude": req.longitude,
        "hourly": "temperature_2m,precipitation",
        "timezone": "auto"
    }
    resp = requests.get(OPENMETEO_URL, params=params)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    data = resp.json()
    # Retorna apenas parte dos dados para simplificar
    return {
        "latitude": req.latitude,
        "longitude": req.longitude,
        "hourly": {
            "time": data["hourly"]["time"][:24],               # Mostra as 24 horas previstas
            "temperature_2m": data["hourly"]["temperature_2m"][:24],
            "precipitation": data["hourly"]["precipitation"][:24]
        }
    }
