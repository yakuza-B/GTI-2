import streamlit as st
from PIL import Image

# Load an image (replace with a relevant file path)
image = Image.open("istockphoto-106492379-612x612.jpg")

# Set page title and layout
st.set_page_config(page_title="Global Terrorism Dashboard", layout="wide")

# Introduction Section
st.title("🌍 Global Terrorism Index 2023 Dashboard")

st.image(image, use_column_width=True)

st.markdown(
    """
    ## Understanding Global Terrorism Trends
    Welcome to the **Global Terrorism Index 2023 Dashboard**, where we analyze and visualize key insights from the latest terrorism data worldwide. 
    
    ### 📌 What You'll Find Here:
    - **Interactive Visualizations** of terrorism incidents across different countries.
    - **Trend Analysis** of incidents over the years.
    - **Impact Assessment** based on fatalities, injuries, and hostage cases.
    
    This dashboard aims to provide a **data-driven perspective** on global security and help policymakers, researchers, and analysts better understand terrorism trends.
    
    👉 Use the sidebar to navigate through the sections.
    """
)
