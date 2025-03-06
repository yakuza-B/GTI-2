import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- TITLE ---
st.title("Global Terrorism Analysis Dashboard")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload Global Terrorism Index CSV", type=["csv"])

if uploaded_file is not None:
    # Load dataset
    data = pd.read_csv(uploaded_file)

    # Show dataset preview
    st.write("### Dataset Preview")
    st.write(data.head())

    # --- TOP 10 COUNTRIES WITH HIGHEST INCIDENTS ---
    st.write("### Top 10 Countries with Highest Terrorism Incidents")

    # Check if 'country' and 'incident_count' columns exist
    if 'country' in data.columns and 'incident_count' in data.columns:
    
