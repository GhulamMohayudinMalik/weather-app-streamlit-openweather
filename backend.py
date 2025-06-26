import requests
import os
import streamlit as st

try:
    # Try loading from Streamlit Cloud secrets
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
except Exception:
    # Fallback to local .env file
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Bahawalpur", 2))