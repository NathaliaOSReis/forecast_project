from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

app = FastAPI(title="Consulta a previsão do tempo básica (temperatura & chuva) para a latitude/longitude fornecidas.")

# Obtém variáveis de ambiente
OPENMETEO_URL = os.getenv("OPENMETEO_URL")
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = os.getenv("API_PORT", "8000")

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
    # Desativa a verificação SSL para fins de teste
    resp = requests.get(OPENMETEO_URL, params=params, verify=False)
    # Suprime avisos relacionados à desativação da verificação SSL
    import warnings
    warnings.filterwarnings("ignore", message="Unverified HTTPS request")
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


