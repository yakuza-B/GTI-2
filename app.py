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
import plotly.graph_objects as go
    






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








# Overview Page
if page == "Overview":
    # Centered Title
    st.markdown("<h1 class='title'>ð � � �  Global Terrorism Overview</h1>", unsafe_allow_html=True)
    
    # Region Selection
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
    
    # Define countries per region
    region_countries = {
        "NA": ["United States", "Canada", "Mexico"],
        "EU": ["United Kingdom", "Germany", "France", "Italy", "Spain", "Netherlands", "Sweden"],
        "SA": ["Brazil", "Argentina", "Colombia", "Chile", "Peru"],
        "AF": ["South Africa", "Nigeria", "Egypt", "Kenya", "Ethiopia"],
        "AS": ["China", "India", "Japan", "Indonesia", "Malaysia", "Pakistan"],
        "ME": ["Iran", "Iraq", "Syria", "Saudi Arabia", "Yemen"],
        "OC": ["Australia", "New Zealand", "Fiji", "Papua New Guinea"]
    }
    
    # Filter data based on selected region
    filtered_data = data[data["Country"].isin(region_countries[selected_region])]
    
    # Display Region-Specific Map
    st.subheader(f"Terrorism Incidents in {regions[selected_region]}")
    st.write(f"The map below visualizes terrorism incidents in {regions[selected_region]}. Each country's color intensity corresponds to the number of incidents recorded.")
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
    
    # Text Explanation for the Map
    st.markdown(f"""
    The map above highlights the distribution of terrorism incidents across {regions[selected_region]}. 
    Countries with darker shades indicate higher numbers of incidents, while lighter shades represent fewer incidents. 
    This visualization helps identify regional hotspots and patterns of terrorist activity.
    """)
    
    # Country Selection (Based on Selected Region)
    st.subheader("Select a Country")
    selected_country = st.selectbox("Choose a country:", region_countries[selected_region])
    
    # Insights from Dataset
    st.subheader(f"Insights for {selected_country}")
    country_data = data[data["Country"] == selected_country]
    if not country_data.empty:
        incidents = country_data["Incidents"].sum()
        most_common_attack = country_data["Attack Type"].mode()[0] if "Attack Type" in country_data else "N/A"
        
        # Graph: Bar Chart for Incident Distribution
        st.write(f"The bar chart below shows the distribution of terrorism incidents in {selected_country}.")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x="Year", y="Incidents", data=country_data, palette="Blues_d", ax=ax)
        ax.set_title(f"Terrorism Incidents Over Time in {selected_country}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Number of Incidents")
        st.pyplot(fig)
        
        # Table: Key Metrics
        st.subheader("Key Metrics")
        metrics_table = pd.DataFrame({
            "Metric": ["Total Incidents", "Most Common Attack Type"],
            "Value": [f"{incidents:,}", most_common_attack]
        })
        st.dataframe(metrics_table)
        
        # Text Explanation for Insights
        st.markdown(f"""
        **Total Incidents**: {selected_country} has recorded a total of {incidents:,} terrorism incidents.  
        **Most Common Attack Type**: The predominant attack type in {selected_country} is `{most_common_attack}`.  
        
        These insights provide a snapshot of the terrorism landscape in {selected_country}, highlighting both the scale and nature of attacks.
        """)
    else:
        st.warning("No data available for the selected country.")
    
    st.markdown("---")  # Divider




  



if page == "Prediction":
    sns.set_style("whitegrid")
    sns.set_palette("Set2")
    
    # Title for the Prediction Page
    st.markdown("<p class='title'> Terrorism Incident Prediction</p>", unsafe_allow_html=True)
    st.write("""
    This application predicts future terrorism incidents using **SARIMA (Seasonal ARIMA)**, 
    a robust time-series forecasting model. It captures trends, seasonality, and irregular patterns 
    in historical data to provide accurate predictions.
    """)

    # Section: Top 5 Countries with the Most Incidents
    st.subheader("Top 5 Countries with the Most Terrorism Incidents")
    st.write("""
    Below is an interactive bar chart showing the top 5 countries with the highest number of terrorism incidents. 
    These countries are identified based on the total number of incidents recorded in the dataset.
    """)
    
    # Aggregate data for top 5 countries
    top_countries = (
        data.groupby("Country")["Incidents"].sum()
        .reset_index()
        .sort_values(by="Incidents", ascending=False)
        .head(5)
    )
    
    # Create an interactive bar chart using Plotly
    fig_top5 = go.Figure()

    # Add bars
    fig_top5.add_trace(go.Bar(
        x=top_countries["Incidents"],
        y=top_countries["Country"],
        orientation="h",  # Horizontal bar chart
        marker=dict(color=top_countries["Incidents"], colorscale="Reds"),  # Gradient color scale
        text=top_countries["Incidents"],  # Display incident counts on bars
        textposition="outside",  # Position text outside the bars
    ))

    # Update layout
    fig_top5.update_layout(
        title="Top 5 Countries with the Most Terrorism Incidents",
        xaxis_title="Total Incidents",
        yaxis_title="Country",
        font=dict(size=14, family="Arial, sans-serif"),
        template="plotly_white",  # Clean white theme
        margin=dict(l=100, r=50, t=80, b=50),  # Adjust margins for spacing
        hovermode="y unified",  # Show hover info for all traces at once
    )

    # Show the interactive plot
    st.plotly_chart(fig_top5, use_container_width=True)

    # Display the top 5 countries as a table
    st.subheader("Top 5 Countries with the Most Terrorism Incidents Data")
    st.dataframe(top_countries)

    # Section: Country-Specific Prediction
    st.subheader("Predict Future Terrorism Incidents for a Specific Country")
    st.write("""
    Use the dropdown menu below to select a country and predict future terrorism incidents.
    """)
    
    # Country selection
    selected_country = st.selectbox("Select a country:", sorted(data["Country"].unique()))
    
    # Filter data by the selected country
    country_data = data[data["Country"] == selected_country]
    if country_data.empty:
        st.warning("No data available for the selected country.")
    else:
        # Group by Year and sum incidents
        incidents_by_year = country_data.groupby("Year")["Incidents"].sum().reset_index()
        if incidents_by_year.empty or incidents_by_year["Incidents"].sum() == 0:
            st.warning(f"No incidents recorded for {selected_country}. Unable to make predictions.")
        elif len(incidents_by_year) < 5:
            st.warning(f"Not enough data to make predictions for {selected_country}.")
        else:
            # Ensure data is sorted by year
            incidents_by_year = incidents_by_year.sort_values(by="Year")
            
            # Fit the SARIMA model
            try:
                model = SARIMAX(
                    incidents_by_year["Incidents"],
                    order=(1, 1, 1),  # Non-seasonal part: (p, d, q)
                    seasonal_order=(1, 1, 1, 12),  # Seasonal part: (P, D, Q, S)
                    enforce_stationarity=False,
                    enforce_invertibility=False
                )
                fit = model.fit(disp=False)
            except Exception as e:
                st.error(f"Model fitting failed: {e}")
                st.stop()
            
            # User input for number of years to predict
            num_years_to_predict = st.slider("Select number of years to predict:", 1, 10, 5)
            last_year = incidents_by_year["Year"].max()
            forecast_years = list(range(last_year + 1, last_year + num_years_to_predict + 1))
            
            # Generate forecasts
            forecast = fit.get_forecast(steps=num_years_to_predict)
            forecast_values = np.maximum(forecast.predicted_mean, 0)  # Ensure non-negative predictions
            
            # Improved graph visualization using Plotly
            fig = go.Figure()

            # Add actual data
            fig.add_trace(go.Scatter(
                x=incidents_by_year["Year"],
                y=incidents_by_year["Incidents"],
                mode="lines+markers",
                name="Actual Data",
                line=dict(color="#4C72B0", width=2),
                marker=dict(size=8)
            ))

            # Add forecasted data
            fig.add_trace(go.Scatter(
                x=forecast_years,
                y=forecast_values,
                mode="lines+markers",
                name="Forecast",
                line=dict(color="green", width=2, dash="dash"),
                marker=dict(size=8)
            ))

            # Update layout
            fig.update_layout(
                title=f"Incident Prediction for {selected_country}",
                xaxis_title="Year",
                yaxis_title="Total Incidents",
                font=dict(size=14, family="Arial, sans-serif"),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                hovermode="x unified",  # Show hover info for all traces at once
                template="plotly_white",  # Clean white theme
                margin=dict(l=50, r=50, t=80, b=50)  # Adjust margins for spacing
            )

            # Add explanatory text above the graph
            st.subheader("Incident Prediction Graph")
            st.write("""
            The graph below shows the historical and predicted terrorism incidents for the selected country. By default will show the incidents from year 2012 to 2022 
            - **Blue Line**: Represents the actual number of incidents recorded in previous years.
            - **Green Dashed Line**: Represents the forecasted number of incidents for future years.
            - Hover over the data points to see exact values for each year.
            
            Note: The predictions are based on the SARIMA model and may not account for unforeseen events or changes in trends.
            """)
            
            # Show the interactive plot
            st.plotly_chart(fig, use_container_width=True)
            
            # Display forecast values without upper/lower bounds
            st.subheader(f"Predicted Incidents for {selected_country}:")
            predictions = pd.DataFrame({
                "Year": forecast_years,
                "Predicted Incidents": forecast_values
            })
            st.dataframe(predictions)
            
            # Model Evaluation Metrics
            residuals = fit.resid
            mae = np.mean(np.abs(residuals))
            rmse = np.sqrt(np.mean(residuals**2))
            st.subheader("Model Evaluation Metrics")
            st.write(f"- **Mean Absolute Error (MAE)**: {mae:.2f}")
            st.write(f"- **Root Mean Squared Error (RMSE)**: {rmse:.2f}")




















