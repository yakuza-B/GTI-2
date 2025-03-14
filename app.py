import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image
import base64
import streamlit as st
from statsmodels.tsa.holtwinters import Holt
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
    






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
page = st.sidebar.radio("Go to", ["About Us", "Introduction", "Overview", "EDA", "Prediction"])


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


elif page == "EDA":
    # Apply Seaborn theme for better aesthetics
    sns.set_style("whitegrid")
    sns.set_palette("Set2")

    st.markdown("<p class='title'>🔍 Exploratory Data Analysis (EDA)</p>", unsafe_allow_html=True)
    
    # Create tabs for different EDA sections
    tab1, tab2, tab3 = st.tabs(["📌 Top 10 Countries", "📊 Data Exploration", "📈 Visualization"])

    # 📌 Top 10 Most Affected Countries
    with tab1:
        st.markdown("## 📌 Top 10 Most Affected Countries")
        
        # Aggregating data to find top affected countries
        country_counts = data.groupby("Country")["Incidents"].sum().reset_index()
        top_countries = country_counts.sort_values(by="Incidents", ascending=False).head(10)

        # Display bar chart
        st.bar_chart(top_countries.set_index("Country"))

        # Data Table
        st.subheader("Top 10 Countries Data")
        st.write(top_countries)

        # Alternative visualization with Seaborn
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x="Incidents", y="Country", data=top_countries, palette="Reds_r", ax=ax)
        ax.set_xlabel("Number of Incidents")
        ax.set_ylabel("Country")
        ax.set_title("Top 10 Countries with Highest Terrorism Incidents")
        st.pyplot(fig)

    # 📊 General Data Exploration
    with tab2:
        st.markdown("## 🔍 Explore the Data")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📍 Incidents by Country")
            st.write(data["Country"].value_counts())

        with col2:
            st.subheader("📆 Incidents by Year")
            st.write(data["Year"].value_counts())

    # 📈 Visualization of Terrorism Trends
    with tab3:
        st.markdown("## 📈 Visualizing Terrorism Trends")

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
        fig = px.choropleth(
            data, 
            locations="iso3c", 
            color="Incidents",
            hover_name="Country",
            title="Global Terrorism Intensity",
            color_continuous_scale="Reds",
            projection="natural earth"
        )
        st.plotly_chart(fig)






  





if page == "Prediction":
    sns.set_style("whitegrid")
    sns.set_palette("Set2")
    st.markdown("<p class='title'>📈 Terrorism Incident Prediction</p>", unsafe_allow_html=True)
    st.write("""
    This application predicts future terrorism incidents using a **Random Forest Regressor**. 
    It leverages historical data, including features like year, fatalities, injuries, and region, 
    to forecast the number of incidents.
    """)

    # Country selection
    selected_country = st.selectbox("Select a country:", sorted(data["Country"].unique()))

    # Filter data by the selected country
    country_data = data[data["Country"] == selected_country]
    if country_data.empty:
        st.warning("No data available for the selected country.")
    else:
        # Prepare the data for modeling
        X = data[['Year', 'Fatalities', 'Injuries', 'Hostages'] + [col for col in data.columns if col.startswith('Region_')]]
        y = data['Incidents']

        # Split into training and testing sets
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the Random Forest Regressor model
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # User input for the year to predict
        future_year = st.slider("Select the year to predict:", 2023, 2030, 2025)

        # Region encoding for the selected country
        selected_region = categorize_region(selected_country)
        region_columns = [col for col in X_train.columns if col.startswith('Region_')]
        region_encoded = {col: 1 if col == f"Region_{selected_region}" else 0 for col in region_columns}

        # Create future_data DataFrame for prediction
        future_data = pd.DataFrame({
            'Year': [future_year],
            'Fatalities': [country_data['Fatalities'].mean()],  # Use mean fatalities as an example
            'Injuries': [country_data['Injuries'].mean()],      # Use mean injuries as an example
            'Hostages': [country_data['Hostages'].mean()]       # Use mean hostages as an example
        })

        # Add region columns to future_data
        future_data = future_data.assign(**region_encoded)

        # Reorder columns to match X_train
        future_data = future_data[X_train.columns]

        # Predict incidents
        future_incidents = model.predict(future_data)[0]

        # Display the prediction
        st.subheader(f"Predicted Incidents for {selected_country} in {future_year}:")
        st.metric("Predicted Incidents", round(future_incidents))

        # Visualize actual vs predicted trends
        st.subheader("Historical vs Predicted Trends")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(country_data['Year'], country_data['Incidents'], marker="o", color="#4C72B0", label="Actual Data")
        ax.scatter([future_year], [future_incidents], color="green", s=100, label="Predicted Value")
        ax.set_title(f"Terrorism Incidents Over Time for {selected_country}", fontsize=16)
        ax.set_xlabel("Year", fontsize=14)
        ax.set_ylabel("Total Incidents", fontsize=14)
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        # Model Evaluation Metrics
        from sklearn.metrics import mean_absolute_error, mean_squared_error
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        st.subheader("Model Evaluation Metrics")
        st.write(f"- **Mean Absolute Error (MAE)**: {mae:.2f}")
        st.write(f"- **Root Mean Squared Error (RMSE)**: {rmse:.2f}")























