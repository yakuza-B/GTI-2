import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

# Load Data
data = pd.read_csv("Global Terrorism Index 2023.csv")

# Load Image for Introduction Page
image = Image.open("istockphoto-106492379-612x612.jpg")

# Set page title and layout
st.set_page_config(page_title="Global Terrorism Dashboard", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #C70039; }
        .metric-box { border-radius: 10px; padding: 15px; background-color: #f0f2f6; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Tab Navigation
tabs = st.tabs(["Introduction", "Overview", "Top 10 Countries", "Data Exploration", "Visualization"])

# Introduction Page
with tabs[0]:
    st.markdown("<p class='title'>🌍 Global Terrorism Index 2023 Dashboard</p>", unsafe_allow_html=True)
    st.image(image, use_column_width=True)
    st.write("""
    ## Global Terrorism Index Dashboard
    Welcome to the **Global Terrorism Index Dashboard**. This application provides insights into terrorism incidents worldwide using data from **2023**.
    
    ### 🔹 Key Features:
    - 📊 Overview of terrorism incidents by country and year.
    - 🔎 Data exploration tools to analyze trends.
    - 📉 Interactive visualizations, including heatmaps and time series charts.
    - 🌍 Highlights of the top 10 most affected countries.
    
    Navigate through the sections using the tabs above.
    """)

    # Poll Question
    st.subheader("📊 Here's a quick question")
    st.write("Which country do you think had the highest number of terrorism incidents in 2023?")
    options = ["Afghanistan", "Iraq", "Nigeria", "Pakistan", "Syria", "India", "Somalia", "Philippines"]
    answer = st.radio("Select an answer:", options)
    if answer:
        if answer == "Afghanistan":
            st.success("✅ Correct! Afghanistan had the highest number of terrorism incidents in 2023.")
        else:
            st.error("❌ Incorrect. The correct answer is Afghanistan.")

# Overview Page
with tabs[1]:
    st.markdown("<p class='title'>📊 Overview of Global Terrorism</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Incidents", data["Incidents"].sum())
    with col2:
        st.metric("Countries Affected", data["Country"].nunique())
    with col3:
        st.metric("Most Affected Country", data.groupby("Country")["Incidents"].sum().idxmax())
    
    st.subheader("Dataset Overview")
    st.write(data.head())

# Top 10 Countries Page
with tabs[2]:
    st.markdown("<p class='title'>🔥 Top 10 Countries with Highest Terrorism Incidents</p>", unsafe_allow_html=True)
    incidents_by_country = data.groupby("Country")["Incidents"].sum().reset_index()
    incidents_by_country = incidents_by_country.sort_values(by="Incidents", ascending=False).head(10)
    fig = px.bar(incidents_by_country, x="Incidents", y="Country", orientation='h', color="Incidents", color_continuous_scale="Reds")
    st.plotly_chart(fig)

# Data Exploration Page
with tabs[3]:
    st.markdown("<p class='title'>🔍 Data Exploration</p>", unsafe_allow_html=True)
    country_filter = st.selectbox("Select a Country", options=data["Country"].unique())
    filtered_data = data[data["Country"] == country_filter]
    st.write(filtered_data)

# Visualization Page
with tabs[4]:
    st.markdown("<p class='title'>📈 Visualizing Terrorism Trends</p>", unsafe_allow_html=True)
    incidents_by_year = data.groupby("Year")["Incidents"].sum().reset_index()
    fig = px.line(incidents_by_year, x="Year", y="Incidents", markers=True, title="Trend of Terrorism Incidents Over Time")
    st.plotly_chart(fig)
    
    fig = px.choropleth(data, locations="iso3c", color="Incidents", hover_name="Country", title="Global Terrorism Intensity", color_continuous_scale="Reds", projection="natural earth")
    st.plotly_chart(fig)
