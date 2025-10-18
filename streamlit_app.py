import streamlit as st
import pandas as pd
import requests

st.title("Earthquake Alert Prediction")

magnitude = st.number_input("Magnitude",)
depth = st.number_input("Depth",)
cdi = st.number_input("CDI",)
mmi = st.number_input("MMI",)
sig = st.number_input("SIG",)

FLASK_URL = "http://127.0.0.1:5000/predict" 
if st.button("Predict Alert"):
    data = {
        "magnitude": magnitude,
        "depth": depth,
        "cdi": cdi,
        "mmi": mmi,
        "sig": sig
    }
    
    try:
        response = requests.post(FLASK_URL, json=data)
        result = response.json()
        
        alert_color = result.get("predicted_alert", "Unknown")
        st.success(f"Predicted Alert: {alert_color}")
        
        
    except Exception as e:
        st.error(f"Error connecting to Flask API: {e}")
