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

# Set Page Title and Layout
st.set_page_config(page_title="Global Terrorism Dashboard", layout="wide")

# Custom CSS for Styled Title and Sidebar
st.markdown("""
    <style>
        /* Global Styles */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
        }
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #C70039;
            margin-bottom: 30px;
            letter-spacing: 1px;
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            color: #333333;
            margin-bottom: 20px;
        }
        .section-header {
            font-size: 28px;
            font-weight: bold;
            color: #4CAF50;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
            padding: 20px;
            border-radius: 10px;
        }
        .metric-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .question-box {
            font-size: 20px;
            font-weight: bold;
            color: #333333;
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .plot-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go to", ["About Us", "Introduction", "Overview", "Top 10 Countries", "Data Exploration", "Visualization"])


# 🌟 About Us Page
if page == "About Us":
    st.markdown("<p class='title'>ℹ️ About Us</p>", unsafe_allow_html=True)

    # Welcome Message
    st.markdown("""
    <p class='subtitle'>
        Welcome to Our Interactive Global Terrorism Index 2023 Dashboard!  
        This platform provides comprehensive insights into global terrorism trends using data-driven analysis.
    </p>
    """, unsafe_allow_html=True)

    # Dataset Information
    st.markdown("<p class='section-header'>📊 Preprocessed Global Terrorism Index Dataset</p>", unsafe_allow_html=True)
    st.write(f"""
    - **Number of Rows**: {len(data):,}  
    - **Key Features**: Country, Year, Incidents, Fatalities, Injuries, Hostages  
    - **Purpose**: To analyze and visualize terrorism trends across different dimensions.
    """)

    # Display Full Dataset (Optional)
    if st.checkbox("Show Full Dataset"):
        st.dataframe(data)  # Show the entire dataset

    # Download Option for Full Dataset
    st.markdown("<p class='section-header'>📥 Download Full Dataset</p>", unsafe_allow_html=True)
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Dataset as CSV",
        data=csv,
        file_name="Global_Terrorism_Index_2023.csv",
        mime="text/csv"
    )

    # Metrics Section
    st.markdown("<p class='section-header'>📈 Key Metrics</p>", unsafe_allow_html=True)
    total_incidents = data["Incidents"].sum()
    total_fatalities = data["Fatalities"].sum()
    total_injuries = data["Injuries"].sum()
    years_covered = data["Year"].nunique()

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='metric-box'>📌 Total Incidents Recorded<br><span style='font-size: 24px; font-weight: bold;'>{:,}</span></div>".format(total_incidents), unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-box'>💀 Total Fatalities<br><span style='font-size: 24px; font-weight: bold;'>{:,}</span></div>".format(total_fatalities), unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='metric-box'>🚑 Total Injuries<br><span style='font-size: 24px; font-weight: bold;'>{:,}</span></div>".format(total_injuries), unsafe_allow_html=True)

    st.write(f"🔹 **Years Covered**: {years_covered}")

    # Submitted By Section
    st.markdown("<p class='section-header'>📝 Submitted By:</p>", unsafe_allow_html=True)
    st.markdown("""
    - **Bernard**  
    - **Barry**   
    - **Travis**  
    """)


# 🎯 Introduction Page
elif page == "Introduction":
    st.markdown("<p class='title'>🌍 Global Terrorism Index 2023 Dashboard</p>", unsafe_allow_html=True)
    
    # Center Image
    st.image(image, use_column_width=True)

    # Introduction Text
    st.markdown("""
    <p class='subtitle'>
        Welcome to the **Global Terrorism Index Dashboard**, which provides insights into terrorism incidents worldwide using **2023** data.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 🔹 **Key Features**
    - 📌 Overview of terrorism incidents by **country** and **year**.
    - 🔍 Interactive tools for **data exploration**.
    - 📊 **Heatmaps & time-series charts** to identify patterns.
    - 🌎 **Top 10 most affected countries** with deep insights.
    
    Navigate through the sections using the sidebar. 📂
    """)

    # Poll Question
    st.markdown("<p class='question-box'>Which country had the highest number of terrorism incidents in 2023?</p>", unsafe_allow_html=True)

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
    
    if st.button("Submit Answer"):
        if answer == "Afghanistan":
            st.success("✅ Correct! Afghanistan had the highest number of terrorism incidents in 2023.")
        else:
            st.error("❌ Incorrect. The correct answer is Afghanistan.")


# 📊 Overview Page
elif page == "Overview":
    st.markdown("<p class='title'>📊 Overview of Global Terrorism</p>", unsafe_allow_html=True)

    # Quick Stats
    total_incidents = data["Incidents"].sum()
    affected_countries = data["Country"].nunique()

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='metric-box'>🌍 Total Incidents Recorded<br><span style='font-size: 24px; font-weight: bold;'>{:,}</span></div>".format(total_incidents), unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-box'>🗺️ Countries Affected<br><span style='font-size: 24px; font-weight: bold;'>{}</span></div>".format(affected_countries), unsafe_allow_html=True)

    st.markdown("<p class='section-header'>Dataset Overview</p>", unsafe_allow_html=True)
    st.dataframe(data.head())


# 🔥 Top 10 Countries Page
elif page == "Top 10 Countries":
    st.markdown("<p class='title'>🔥 Top 10 Most Affected Countries</p>", unsafe_allow_html=True)
    
    # Group by Country and Sum Incidents
    incidents_by_country = data.groupby("Country")["Incidents"].sum().reset_index()
    incidents_by_country = incidents_by_country.sort_values(by="Incidents", ascending=False).head(10)
    
    # Display Data
    st.markdown("<p class='section-header'>📊 Top 10 Countries by Incidents</p>", unsafe_allow_html=True)
    st.dataframe(incidents_by_country, height=300)

    # Bar Chart
    st.markdown("<p class='section-header'>📈 Bar Chart Visualization</p>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="Incidents", y="Country", data=incidents_by_country, palette="Reds_r", ax=ax)
    ax.set_xlabel("Number of Incidents")
    ax.set_ylabel("Country")
    ax.set_title("Top 10 Countries with Highest Terrorism Incidents")
    st.pyplot(fig)


# 🔍 Data Exploration Page
elif page == "Data Exploration":
    st.markdown("<p class='title'>🔍 Explore the Data</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<p class='section-header'>📍 Incidents by Country</p>", unsafe_allow_html=True)
        st.write(data["Country"].value_counts())

    with col2:
        st.markdown("<p class='section-header'>📆 Incidents by Year</p>", unsafe_allow_html=True)
        st.write(data["Year"].value_counts())


# 📈 Visualization Page
elif page == "Visualization":
    st.markdown("<p class='title'>📈 Visualizing Terrorism Trends</p>", unsafe_allow_html=True)
    
    # Group by Year and Sum Incidents
    incidents_by_year = data.groupby("Year")["Incidents"].sum().reset_index()
    
    # Line Chart
    st.markdown("<p class='section-header'>📊 Trend Over Time</p>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="Year", y="Incidents", data=incidents_by_year, marker="o", color="red", ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Incidents")
    ax.set_title("Trend of Terrorism Incidents Over Time")
    ax.grid(True)
    st.pyplot(fig)
    
    # World Heatmap (Choropleth)
    st.markdown("<p class='section-header'>🌍 Global Terrorism Intensity</p>", unsafe_allow_html=True)
    fig = px.choropleth(data, 
                        locations="iso3c", 
                        color="Incidents",
                        hover_name="Country",
                        title="Global Terrorism Intensity",
                        color_continuous_scale="Reds",
                        projection="natural earth")
    st.plotly_chart(fig)
