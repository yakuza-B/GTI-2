import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv("Global Terrorism Index 2023.csv")

# Set Streamlit page config
st.set_page_config(page_title="Global Terrorism Dashboard", layout="wide")

# Title and description
st.title("Global Terrorism Index 2023 Dashboard")
st.markdown("""
This interactive dashboard provides insights into global terrorism incidents, trends, and impacts.

### Key Features:
- View the top 10 countries with the highest terrorism incidents.
- Explore trends over time.
- Analyze the correlation between terrorism-related factors.
""")

# Sidebar Filters
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", options=sorted(data["Year"].unique(), reverse=True))

# Filter data based on selected year
data_filtered = data[data["Year"] == selected_year]

# **Top 10 Countries with Highest Terrorism Incidents**
st.subheader(f"Top 10 Countries with Highest Terrorism Incidents in {selected_year}")
incidents_by_country = data_filtered.groupby("Country")["Incidents"].sum().reset_index()
incidents_by_country = incidents_by_country.sort_values(by="Incidents", ascending=False).head(10)

# Plot Bar Chart
fig_top10 = px.bar(incidents_by_country, x="Incidents", y="Country", orientation='h',
                    title=f"Top 10 Countries with Highest Terrorism Incidents in {selected_year}",
                    labels={"Incidents": "Number of Incidents", "Country": "Country"},
                    color="Incidents", color_continuous_scale="Reds")
st.plotly_chart(fig_top10, use_container_width=True)

# **Terrorism Trend Over Time**
st.subheader("Terrorism Incidents Over Time")
incidents_by_year = data.groupby("Year")["Incidents"].sum().reset_index()
fig_trend = px.line(incidents_by_year, x="Year", y="Incidents", markers=True,
                     title="Trend of Terrorism Incidents Over Time")
st.plotly_chart(fig_trend, use_container_width=True)

# **World Heatmap of Incidents**
st.subheader("Global Terrorism Intensity")
fig_map = px.choropleth(data, locations="iso3c", color="Incidents",
                        hover_name="Country", title="Global Terrorism Intensity",
                        color_continuous_scale="Reds", projection="natural earth")
st.plotly_chart(fig_map, use_container_width=True)

st.write("---")
st.write("Data Source: Global Terrorism Index 2023")
