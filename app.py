import streamlit as st
import pandas as pd

from modules.iss_monitor import get_iss_position
from modules.nbtc_data import load_nbtc_data, validate_nbtc_csv

st.set_page_config(page_title="ISS + NBTC Dashboard", page_icon="🛰️", layout="wide")
st.title("🛰️ ISS + NBTC Public Information Dashboard")
st.caption("Educational prototype using public information. Not an official NASA or NBTC service.")

left, right = st.columns(2)

with left:
    st.subheader("International Space Station")
    if st.button("Refresh ISS position"):
        st.cache_data.clear()

    try:
        iss = get_iss_position()
        a, b, c = st.columns(3)
        a.metric("Latitude", f"{iss['latitude']:.4f}°")
        b.metric("Longitude", f"{iss['longitude']:.4f}°")
        c.metric("Altitude", f"{iss['altitude']:.1f} km")
        st.metric("Orbital speed", f"{iss['velocity']:.1f} km/h")
        st.map(pd.DataFrame({"lat": [iss["latitude"]], "lon": [iss["longitude"]]}), zoom=1)
        st.markdown("[View ISS API source](https://api.wheretheiss.at/v1/satellites/25544)")
    except Exception as exc:
        st.warning("Live ISS information is unavailable right now.")
        st.caption(f"Details: {exc}")

with right:
    st.subheader("NBTC public information")
    st.write(
        "Load a dataset published for public use by NBTC. The included CSV contains "
        "illustrative sample rows only; it is not official NBTC statistics."
    )
    nbtc = load_nbtc_data()
    if nbtc.empty:
        st.info("No NBTC dataset is available yet.")
    else:
        st.dataframe(nbtc, use_container_width=True, hide_index=True)
        if "topic" in nbtc.columns and "value" in nbtc.columns:
            st.bar_chart(nbtc.set_index("topic")["value"])
    st.markdown("[NBTC official website](https://www.nbtc.go.th/)")

st.divider()
st.subheader("Import a public NBTC CSV dataset")
st.write("Required columns: date, topic, value, unit, source_url")
uploaded = st.file_uploader("Choose CSV file", type=["csv"])
if uploaded:
    try:
        imported = pd.read_csv(uploaded)
        valid, message = validate_nbtc_csv(imported)
        if valid:
            st.success("CSV structure validated. Review the source and data before using it.")
            st.dataframe(imported, use_container_width=True)
            st.download_button(
                "Download validated CSV",
                imported.to_csv(index=False).encode("utf-8"),
                file_name="nbtc_public_data.csv",
                mime="text/csv",
            )
        else:
            st.error(message)
    except Exception as exc:
        st.error(f"Could not read CSV: {exc}")

st.caption("Always verify publication date, licence, definitions, and methodology of external datasets.")
