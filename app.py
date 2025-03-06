import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Data
data = pd.read_csv("Global Terrorism Index 2023.csv")

from PIL import Image

# Load an image (replace with a relevant file path)
image = Image.open("terrorism_index.jpg")

# Set page title and layout
st.set_page_config(page_title="Global Terrorism Dashboard", layout="wide")

# Introduction Section
st.title("🌍 Global Terrorism Index 2023 Dashboard")

st.image(image, use_column_width=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Overview", "Top 10 Countries", "Data Exploration", "Visualization"])

# Introduction Page
if page == "Introduction":
    st.title("Introduction")
    st.write("""
    ## Global Terrorism Index Dashboard
    Welcome to the Global Terrorism Index Dashboard. This application provides insights into terrorism incidents 
    across the world, using data from the Global Terrorism Index 2023.
    
    ### Key Features:
    - Overview of terrorism incidents by country and year.
    - Data exploration tools to understand patterns.
    - Interactive visualizations, including heatmaps and trend analysis.
    - Top 10 most affected countries with terrorism incidents.
    
    Navigate through the sections using the sidebar to explore different aspects of terrorism data.
    """)

# Overview Page
elif page == "Overview":
    st.title("Overview of Global Terrorism")
    st.write("Here, you can explore general statistics and trends on terrorism incidents globally.")
    
    st.subheader("Dataset Information")
    st.write(data.head())
    st.write("### Missing Values")
    st.write(data.isnull().sum())
    
    st.subheader("Basic Statistics")
    st.write(data.describe())

# Top 10 Countries Page
elif page == "Top 10 Countries":
    st.title("Top 10 Countries with Highest Terrorism Incidents")
    
    # Group by country and sum incidents
    incidents_by_country = data.groupby("Country")["Incidents"].sum().reset_index()
    incidents_by_country = incidents_by_country.sort_values(by="Incidents", ascending=False).head(10)
    
    # Display DataFrame
    st.write(incidents_by_country)
    
    # Bar Chart
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="Incidents", y="Country", data=incidents_by_country, palette="Reds_r", ax=ax)
    ax.set_xlabel("Number of Incidents")
    ax.set_ylabel("Country")
    ax.set_title("Top 10 Countries with Highest Terrorism Incidents")
    st.pyplot(fig)

# Data Exploration Page
elif page == "Data Exploration":
    st.title("Data Exploration")
    
    st.subheader("Frequency Tables")
    st.write("Incidents by Country:")
    st.write(data["Country"].value_counts())
    
    st.write("Incidents by Year:")
    st.write(data["Year"].value_counts())
    
# Visualization Page
elif page == "Visualization":
    st.title("Visualizing Terrorism Trends")
    
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
