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

# Custom CSS for Centered Title and Styled Sidebar
st.markdown("""
    <style>
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #C70039; }
        .sidebar .sidebar-content { background-color: #f7f7f7; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Overview", "Top 10 Countries", "Data Exploration", "Visualization"])

# Introduction Page
if page == "Introduction":
    st.markdown("<p class='title'>🌍 Global Terrorism Index 2023 Dashboard</p>", unsafe_allow_html=True)
    
    # Center Image
    st.image(image, use_column_width=True)
    
    # Introduction Text
    st.write("""
    ## Global Terrorism Index Dashboard
    Welcome to the **Global Terrorism Index Dashboard**. This application provides insights into terrorism incidents 
    worldwide using data from **2023**.
    
    ### 🔹 Key Features:
    - 📊 Overview of terrorism incidents by country and year.
    - 🔎 Data exploration tools to analyze trends.
    - 📉 Interactive visualizations, including heatmaps and time series charts.
    - 🌍 Highlights of the top 10 most affected countries.
    
    Navigate through the sections using the sidebar to explore different aspects of terrorism data.
    """)


    # Poll Question
    st.subheader("📊 Here's a quick question")
    st.write("Which country do you think had the highest number of terrorism incidents in 2023?")

    options = [
        "Afghanistan", 
        "Iraq", 
        "Nigeria", 
        "Pakistan", 
        "Syria", 
        "India", 
        "Somalia", 
        "Philippines"
    ]

    answer = st.radio("Select an answer:", options)

    if answer:
        if answer == "Afghanistan":
            st.success("✅ Correct! Afghanistan had the highest number of terrorism incidents in 2023.")
        else:
            st.error("❌ Incorrect. The correct answer is Afghanistan.")



# Overview Page
elif page == "Overview":
    st.markdown("<p class='title'>📊 Overview of Global Terrorism</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dataset Information")
        st.write(data.head())

    with col2:
        st.subheader("Missing Values")
        st.write(data.isnull().sum())
    
    st.subheader("Basic Statistics")
    st.write(data.describe())

# Top 10 Countries Page
elif page == "Top 10 Countries":
    st.markdown("<p class='title'>🔥 Top 10 Countries with Highest Terrorism Incidents</p>", unsafe_allow_html=True)
    
    # Group by country and sum incidents
    incidents_by_country = data.groupby("Country")["Incidents"].sum().reset_index()
    incidents_by_country = incidents_by_country.sort_values(by="Incidents", ascending=False).head(10)
    
    # Display DataFrame
    st.dataframe(incidents_by_country)
    
    # Bar Chart
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="Incidents", y="Country", data=incidents_by_country, palette="Reds_r", ax=ax)
    ax.set_xlabel("Number of Incidents")
    ax.set_ylabel("Country")
    ax.set_title("Top 10 Countries with Highest Terrorism Incidents")
    st.pyplot(fig)

# Data Exploration Page
elif page == "Data Exploration":
    st.markdown("<p class='title'>🔍 Data Exploration</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Incidents by Country")
        st.write(data["Country"].value_counts())

    with col2:
        st.subheader("Incidents by Year")
        st.write(data["Year"].value_counts())

# Visualization Page
elif page == "Visualization":
    st.markdown("<p class='title'>📈 Visualizing Terrorism Trends</p>", unsafe_allow_html=True)
    
    # Group by Year and sum incidents
    incidents_by_year = data.groupby("Year")["Incidents"].sum().reset_index()
    
    # Line Chart
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="Year", y="Incidents", data=incidents_by_year, marker="o", color="red", ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Incidents")
    ax.set_title("Trend of Terrorism Incidents Over Time")
    ax.grid(True)
    st.pyplot(fig)
    
    # World Heatmap (Choropleth)
    fig = px.choropleth(data, 
                        locations="iso3c", 
                        color="Incidents",
                        hover_name="Country",
                        title="Global Terrorism Intensity",
                        color_continuous_scale="Reds",
                        projection="natural earth")
    st.plotly_chart(fig)
