import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

st.set_page_config(page_title="Previsão do Tempo", layout="centered")

st.title("🌦️ Previsão do Tempo Amigável")
st.markdown("Digite o nome de uma cidade para obter a previsão do tempo para as próximas horas.")

# Entrada do nome da cidade - deixei São Paulo como exemplo de input
city_name = st.text_input("Cidade:", value="São Paulo")

if st.button("Obter Previsão"):
    if not city_name.strip():
        st.error("Por favor, informe o nome de uma cidade.")
    else:
        # Geocodifica a cidade via Nominatim (OpenStreetMap)
        geocode_url = "https://nominatim.openstreetmap.org/search"
        geocode_params = {"q": city_name, "format": "json", "limit": 1}
        try:
            # Desativa a verificação SSL para fins de teste
            geocode_resp = requests.get(geocode_url, params=geocode_params, headers={"User-Agent": "streamlit-app"}, verify=False)
            geocode_resp.raise_for_status()
            # Suprime avisos relacionados à desativação da verificação SSL
            import warnings
            warnings.filterwarnings("ignore", message="Unverified HTTPS request")
            locations = geocode_resp.json()
            if not locations:
                st.error(f"Cidade '{city_name}' não encontrada. Tente outro nome.")
            else:
                loc = locations[0]
                lat, lon = float(loc['lat']), float(loc['lon'])
                display_name = loc.get('display_name', city_name)

                st.subheader(f"Previsão para: {display_name}")

                # Chama a API local usando variáveis de ambiente
                # No Docker, o nome do serviço 'api' é usado como hostname
                API_HOST = os.getenv("API_HOST", "127.0.0.1")
                API_PORT = os.getenv("API_PORT", "8000")
                API_URL = f"http://{API_HOST}:{API_PORT}/forecast"
                st.info(f"Conectando à API em: {API_URL}")
                payload = {"latitude": lat, "longitude": lon}
                resp = requests.post(API_URL, json=payload)
                try:
                    resp.raise_for_status()
                    data = resp.json()

                    # Constrói o DataFrame e exibe
                    df = pd.DataFrame({
                        "Temperatura (°C)": data["hourly"]["temperature_2m"],
                        "Chuva (mm)": data["hourly"]["precipitation"]
                    }, index=pd.to_datetime(data["hourly"]["time"]))

                    st.line_chart(df)
                    st.dataframe(df)
                except Exception as e:
                    st.error(f"Erro ao obter previsão: {e}")
        except Exception as ge:
            st.error(f"Erro de geocodificação: {ge}")




