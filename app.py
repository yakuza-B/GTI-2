import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Data


data = pd.read_csv("/absolute/path/to/Global Terrorism Index 2023.csv")


st.title("Global Terrorism Index 2023 Dashboard")

# Display Data
st.subheader("Dataset Preview")
st.dataframe(data.head())

# Missing Values
st.subheader("Missing Values in Each Column")
st.write(data.isnull().sum())

# Frequency Tables
st.subheader("Frequency Tables")
st.write("**ISO3C Codes:**", data.iso3c.value_counts())
st.write("**Countries:**", data.Country.value_counts())
st.write("**Rank:**", data.Rank.value_counts())
st.write("**Score:**", data.Score.value_counts())
st.write("**Incidents:**", data.Incidents.value_counts())
st.write("**Fatalities:**", data.Fatalities.value_counts())
st.write("**Injuries:**", data.Injuries.value_counts())
st.write("**Hostages:**", data.Hostages.value_counts())
st.write("**Years:**", data.Year.value_counts())

# Descriptive Statistics
st.subheader("Descriptive Statistics")
st.write(data.describe())

# Visualization 1: Top 10 Countries with Highest Terrorism Incidents
st.subheader("Top 10 Countries with Highest Terrorism Incidents")
incidents_by_country = data.groupby("Country")["Incidents"].sum().reset_index()
incidents_by_country = incidents_by_country.sort_values(by="Incidents", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x="Incidents", y="Country", data=incidents_by_country, palette="Reds_r", ax=ax)
st.pyplot(fig)

# Visualization 2: Terrorism Trend Over Time
st.subheader("Trend of Terrorism Incidents Over Time")
incidents_by_year = data.groupby("Year")["Incidents"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="Year", y="Incidents", data=incidents_by_year, marker="o", color="red", ax=ax)
st.pyplot(fig)

# Visualization 3: Proportion of Fatalities, Injuries, and Hostages
st.subheader("Proportion of Fatalities, Injuries, and Hostages")
impact_data = data[["Fatalities", "Injuries", "Hostages"]].sum()
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(impact_data, labels=impact_data.index, autopct="%1.1f%%", colors=["red", "orange", "yellow"], startangle=140)
st.pyplot(fig)

# Visualization 4: Global Terrorism Intensity Map
st.subheader("Global Terrorism Intensity Map")
fig = px.choropleth(data, locations="iso3c", color="Incidents", hover_name="Country",
                    title="Global Terrorism Intensity", color_continuous_scale="Reds", projection="natural earth")
st.plotly_chart(fig)

# Visualization 5: Correlation Matrix
st.subheader("Correlation Matrix of Terrorism Factors")
numeric_data = data.select_dtypes(include=['number'])
corr_matrix = numeric_data.corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

st.write("### Dashboard Created with Streamlit")
