import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image
import base64
import streamlit as st
import numpy as np
import pickle





# Encode the image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Replace 'your_image.png' with the actual image filename
image_base64 = get_base64_image("istockphoto-106492379-612x612.jpg")


# Load Data
data = pd.read_csv("Global Terrorism Index 2023.csv")

# Load Image for Introduction Page
image = Image.open("istockphoto-106492379-612x612.jpg")

# Set Page Title and Layout
st.set_page_config(page_title="Global Terrorism Dashboard", layout="wide")

#Custom CSS for Styled Title and Sidebar
st.markdown("""
    <style>
        .title { text-align: center; font-size: 36px !important; font-weight: bold; color: white; }
        .sidebar .sidebar-content { background-color: #f7f7f7; }
        .question-box { font-size: 20px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go to", ["About Us", "Introduction", "Overview", "Top 10 Countries", "Data Exploration", "Visualization", "Prediction"])


if page == "About Us":
    st.markdown("<p class='title'>👥 About Us</p>", unsafe_allow_html=True)

    # Welcome Message
    st.write("""
    ## 🌟 Welcome to Our Interactive Global Terrorism Index 2023 Dashboard!
    
    This dashboard is designed to provide a **comprehensive analysis** of global terrorism trends. By leveraging the dataset below, we deliver valuable insights into how various factors such as **country**, **year**, **number of incidents**, **fatalities**, and **injuries** impact the global terrorism landscape.
    """)

    # Dataset Information
    st.subheader("📊 Preprocessed Global Terrorism Index Dataset")
    st.write(f"""
    - **Number of Rows**: {len(data):,}  
    - **Key Features**: Country, Year, Incidents, Fatalities, Injuries, Hostages  
    - **Purpose**: To analyze and visualize terrorism trends across different dimensions.
    """)

    # Display Full Dataset (Optional)
    if st.checkbox("Show Full Dataset"):
        st.dataframe(data)  # Show the entire dataset

    # Download Option for Full Dataset
    st.subheader("📥 Download Full Dataset")
    st.markdown("""
    If you'd like to explore the dataset further, you can download it as a CSV file:
    """)
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Dataset as CSV",
        data=csv,
        file_name="Global_Terrorism_Index_2023.csv",
        mime="text/csv"
    )


    # Additional Metrics
    total_incidents = data["Incidents"].sum()
    total_fatalities = data["Fatalities"].sum()
    total_injuries = data["Injuries"].sum()
    years_covered = data["Year"].nunique()

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="📌 Total Incidents Recorded", value=f"{total_incidents:,}")
    
    with col2:
        st.metric(label="💀 Total Fatalities", value=f"{total_fatalities:,}")
    
    with col3:
        st.metric(label="🚑 Total Injuries", value=f"{total_injuries:,}")

    st.write(f"🔹 **Years Covered**: {years_covered}")

    st.write("🔹 Our goal is to provide valuable insights to enhance awareness and support data-driven decision-making. Thank you for using our dashboard!")


# Submitted By Section
    st.subheader("📝 Submitted By:")
    st.markdown("""
    - **Bernard**  
    - **Barry**   
    - **Travis**  
    """)


# 🎯 Introduction Page
if page == "Introduction":
    st.markdown("<p class='title'>🌍 Global Terrorism Index 2023 Dashboard</p>", unsafe_allow_html=True)
    
    
   
    
    # Center Image 
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="data:image/png;base64,{}" width="500">
    </div>
    """.format(base64.b64encode(open("istockphoto-106492379-612x612.jpg", "rb").read()).decode()),
    unsafe_allow_html=True
)








    # Introduction Text
    st.write("""
    ## 📊 Understanding Global Terrorism Trends
    Terrorism remains one of the most critical global security challenges, affecting **millions of lives** and disrupting societies. 
    The **Global Terrorism Index Dashboard** provides insights into terrorism incidents worldwide using **2023** data.

    ### 🛡️ **What is Terrorism?**
    Terrorism refers to **the unlawful use of violence and intimidation**, especially against civilians, to achieve political, 
    religious, or ideological goals. It often targets governments, infrastructure, and innocent populations to spread fear 
    and influence decision-making.

    ### 🌎 **Global Trends in Terrorism**
    Over the years, terrorism has evolved in scale, tactics, and geographical distribution. Some key trends include:

    - 📈 **Rise and fall of terrorist organizations**: Groups like ISIS, Al-Qaeda, and Boko Haram have shaped global security, while some have weakened due to counterterrorism efforts.
    - 🌍 **Regional Hotspots**: The highest number of terrorist attacks occur in regions like the **Middle East, South Asia, and Africa**.
    - 🔥 **Shifting Strategies**: Terrorist groups have adapted to technology, using social media for propaganda, recruitment, and financing.
    - 📉 **Declining Trends**: Some regions have seen a decrease in attacks due to **strong counterterrorism policies** and **intelligence cooperation**.

    ### 🔹 **Key Features of This Dashboard**
    This dashboard allows users to explore global terrorism trends using real-time data and visualization tools.

    - 📌 **Overview of terrorism incidents** by **country** and **year**.
    - 🔍 **Interactive tools** for analyzing trends and patterns.
    - 📊 **Heatmaps & time-series charts** to understand attack frequency.
    - 🌎 **Insights on the top 10 most affected countries**.

    By studying these trends, policymakers, researchers, and the public can **better understand terrorism and develop 
    strategies to prevent future threats**.

    ---
    """)

    # 🔥 Poll Question
    st.subheader("📊 Quick Question")
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

    # Moved navigation instructions below the poll
    st.markdown("📂 **For more infomation, navigate through the sections using the sidebar.**")








# 📊 Overview Page
if page == "Overview":
    # Centered Title
    st.markdown("<h1 class='title'>🌍 Global Terrorism Overview</h1>", unsafe_allow_html=True)

    # 📍 Region Selection (Now above the map)
    st.subheader("Select a Region")
    regions = {
        "NA": "North America",
        "EU": "Europe",
        "SA": "South America",
        "AF": "Africa",
        "AS": "Asia",
        "ME": "Middle East",
        "OC": "Oceania"
    }
    
    selected_region = st.radio("Map Scope Selection", list(regions.keys()), horizontal=True, format_func=lambda x: regions[x])

    # 🌍 Define countries per region
    region_countries = {
        "NA": ["United States", "Canada", "Mexico"],
        "EU": ["United Kingdom", "Germany", "France", "Italy", "Spain", "Netherlands", "Sweden"],
        "SA": ["Brazil", "Argentina", "Colombia", "Chile", "Peru"],
        "AF": ["South Africa", "Nigeria", "Egypt", "Kenya", "Ethiopia"],
        "AS": ["China", "India", "Japan", "Indonesia", "Malaysia", "Pakistan"],
        "ME": ["Iran", "Iraq", "Syria", "Saudi Arabia", "Yemen"],
        "OC": ["Australia", "New Zealand", "Fiji", "Papua New Guinea"]
    }
    
    # 🌍 Filter data based on selected region
    filtered_data = data[data["Country"].isin(region_countries[selected_region])]

    # 🌍 Display Region-Specific Map
    st.subheader(f"Terrorism Incidents in {regions[selected_region]}")
    
    if not filtered_data.empty:
        fig = px.choropleth(
            data_frame=filtered_data,
            locations="Country",
            locationmode="country names",
            color="Incidents",
            title=f"Terrorism Incidents in {regions[selected_region]}",
            color_continuous_scale="purples",
            template="plotly_dark"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"No data available for {regions[selected_region]}.")

    # 📌 Country Selection (Now based on selected region)
    selected_country = st.selectbox("Select a Country:", region_countries[selected_region])

    # 📊 Insights from dataset
    st.subheader(f"Insights for {selected_country}:")
    country_data = data[data["Country"] == selected_country]

    if not country_data.empty:
        incidents = country_data["Incidents"].sum()
        most_common_attack = country_data["Attack Type"].mode()[0] if "Attack Type" in country_data else "N/A"

        st.markdown(f"🛑 **Total Incidents**: {incidents:,}")
        st.markdown(f"🔥 **Most Common Attack Type**: {most_common_attack}")
    else:
        st.warning("No data available for the selected country.")

    st.markdown("---")  # Divider





  


# 📌 Top 10 Countries Page
elif page == "Top 10 Countries":
    st.markdown("<p class='title'>📌 Top 10 Countries Affected</p>", unsafe_allow_html=True)

    # Aggregating data to find top affected countries
    country_counts = data.groupby("Country")["Incidents"].sum().reset_index()
    top_countries = country_counts.sort_values(by="Incidents", ascending=False).head(10)

    st.bar_chart(top_countries.set_index("Country"))  # Visualizing the top 10 countries

    st.subheader("Top 10 Countries Data")
    st.write(top_countries)



# 🔥 Top 10 Countries Page
elif page == "Top 10 Countries":
    st.markdown("<p class='title'>🔥 Top 10 Most Affected Countries</p>", unsafe_allow_html=True)
    
    # Group by Country and Sum Incidents
    incidents_by_country = data.groupby("Country")["Incidents"].sum().reset_index()
    incidents_by_country = incidents_by_country.sort_values(by="Incidents", ascending=False).head(10)
    
    # Display Data
    st.dataframe(incidents_by_country, height=300)

    # Bar Chart
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
        st.subheader("📍 Incidents by Country")
        st.write(data["Country"].value_counts())

    with col2:
        st.subheader("📆 Incidents by Year")
        st.write(data["Year"].value_counts())

# 📈 Visualization Page
elif page == "Visualization":
    st.markdown("<p class='title'>📈 Visualizing Terrorism Trends</p>", unsafe_allow_html=True)
    
    # Group by Year and Sum Incidents
    incidents_by_year = data.groupby("Year")["Incidents"].sum().reset_index()
    
    # Line Chart
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="Year", y="Incidents", data=incidents_by_year, marker="o", color="red", ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Incidents")
    ax.set_title("Trend of Terrorism Incidents Over Time")
    ax.grid(True)
    st.pyplot(fig)
    
    # 🌍 World Heatmap (Choropleth)
    fig = px.choropleth(data, 
                        locations="iso3c", 
                        color="Incidents",
                        hover_name="Country",
                        title="Global Terrorism Intensity",
                        color_continuous_scale="Reds",
                        projection="natural earth")
    st.plotly_chart(fig)



elif page == "Prediction":
    st.markdown("<h1 class='title'>🔮 Terrorism Incident Prediction</h1>", unsafe_allow_html=True)

    st.subheader("Enter Details to Predict Incident Trends")

    # User Input for Prediction
    year = st.number_input("Year", min_value=1970, max_value=2030, step=1, value=2025)

    # Ensure "Country" exists in the dataset
    if "Country" in data.columns:
        country = st.selectbox("Country", sorted(data["Country"].unique()))
    else:
        st.error("⚠️ 'Country' column is missing in the dataset.")
        country = "Unknown"

    # Convert Categorical Inputs to Numeric
    if 'label_encoder' in globals():
        try:
            country_encoded = label_encoder.transform([country])[0]
        except Exception as e:
            st.error(f"⚠️ Encoding error: {e}")
            country_encoded = 0
    else:
        st.warning("⚠️ Label encoder not found. Using default encoding.")
        country_encoded = 0

    # Prepare Feature Array
    input_features = np.array([[year, country_encoded]])

    # Predict Button
    if st.button("Predict Incident Trend"):
        if model is not None:
            try:
                prediction = model.predict(input_features)
                trend = "Increase" if prediction[0] > 0 else "Decrease"
                st.success(f"Predicted Trend: {trend} in {year}")
            except Exception as e:
                st.error(f"⚠️ Prediction error: {e}")
        else:
            st.error("⚠️ Prediction model is not loaded. Please check the model file.")

    st.markdown("---")  # Divider








