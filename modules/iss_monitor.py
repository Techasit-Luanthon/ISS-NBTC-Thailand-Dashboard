import requests
import streamlit as st

ISS_API_URL = "https://api.wheretheiss.at/v1/satellites/25544"

@st.cache_data(ttl=30)
def get_iss_position():
    """Return the latest publicly available ISS position."""
    response = requests.get(ISS_API_URL, timeout=12)
    response.raise_for_status()
    data = response.json()

    required = ("latitude", "longitude", "altitude", "velocity")
    missing = [key for key in required if key not in data]
    if missing:
        raise ValueError(f"ISS API response missing fields: {', '.join(missing)}")
    return data
