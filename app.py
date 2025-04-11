import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image
import base64
import streamlit as st
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

if page != "EDA":
    if "show_eda" in st.session_state:
        st.session_state.show_eda = False
        
if page == "About Us":
    st.markdown("<p class='title'>👥 About Us</p>", unsafe_allow_html=True)

    # Welcome Message
    st.write("""
    ## 🌟 Welcome to Our Interactive Global Terrorism Index 2023 Dashboard!
    
    This dashboard is designed to provide a *comprehensive analysis* of global terrorism trends. By leveraging the dataset below, we deliver valuable insights into how various factors such as *country, **year, **number of incidents, **fatalities, and **injuries* impact the global terrorism landscape.
    """)

    # Dataset Information
    st.subheader("📊 Preprocessed Global Terrorism Index Dataset")
    st.write(f"""
    - *Number of Rows*: {len(data):,}  
    - *Key Features*: Country, Year, Incidents, Fatalities, Injuries, Hostages  
    - *Purpose*: To analyze and visualize terrorism trends across different dimensions.
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

    st.write(f"🔹 *Years Covered*: {years_covered}")

    st.write("🔹 Our goal is to provide valuable insights to enhance awareness and support data-driven decision-making. Thank you for using our dashboard!")


# Submitted By Section
    st.subheader("📝 Submitted By:")
    st.markdown("""
    - *Bernard*  
    - *Barry*   
    - *Travis*  
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
    Terrorism remains one of the most critical global security challenges, affecting *millions of lives* and disrupting societies. 
    The *Global Terrorism Index Dashboard* provides insights into terrorism incidents worldwide using *2023* data.

    ### 🛡 *What is Terrorism?*
    Terrorism refers to *the unlawful use of violence and intimidation*, especially against civilians, to achieve political, 
    religious, or ideological goals. It often targets governments, infrastructure, and innocent populations to spread fear 
    and influence decision-making.

    ### 🌎 *Global Trends in Terrorism*
    Over the years, terrorism has evolved in scale, tactics, and geographical distribution. Some key trends include:

    - 📈 *Rise and fall of terrorist organizations*: Groups like ISIS, Al-Qaeda, and Boko Haram have shaped global security, while some have weakened due to counterterrorism efforts.
    - 🌍 *Regional Hotspots: The highest number of terrorist attacks occur in regions like the **Middle East, South Asia, and Africa*.
    - 🔥 *Shifting Strategies*: Terrorist groups have adapted to technology, using social media for propaganda, recruitment, and financing.
    - 📉 *Declining Trends: Some regions have seen a decrease in attacks due to **strong counterterrorism policies* and *intelligence cooperation*.

    ### 🔹 *Key Features of This Dashboard*
    This dashboard allows users to explore global terrorism trends using real-time data and visualization tools.

    - 📌 *Overview of terrorism incidents* by *country* and *year*.
    - 🔍 *Interactive tools* for analyzing trends and patterns.
    - 📊 *Heatmaps & time-series charts* to understand attack frequency.
    - 🌎 *Insights on the top 10 most affected countries*.

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
    st.markdown("📂 *For more infomation, navigate through the sections using the sidebar.*")




# 📊 Overview Page
if 'page' in locals() and page == "Overview":
    # Centered Title
    st.markdown("""
    <h1 style='text-align: center; font-size: 45px;'>🌍 Global Terrorism Overview</h1>
    <h3 style='text-align: center; font-size: 20px; color: gray;'>Analyzing global terrorism trends, hotspots, and impacts.</h3>
""", unsafe_allow_html=True)

    # Create a two-column layout (adjust column widths as needed)
    col1, col2 = st.columns([1.2, 2])  # 1: GIF, 2: Text

    with col1:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGhiaTAxOHA4OWdqY2xuaXp2czA3c3UzYTBlbGM2c3R6cXZzbWI3OCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cb89q6BvqAHfwH6AEU/giphy.gif", width=400)

    with col2:
        st.markdown("""
        <p style='font-size: 20px; text-align: justify; line-height: 1.6;'>
        Terrorism is a global threat that evolves with political conflicts, economic disparities, and technological advancements. 
        Regions like the Middle East, Africa, and South Asia remain major hotspots, while cyber and lone-wolf attacks are on the rise. 
        Terrorist groups leverage social media, encrypted communication, and drones, increasing their reach and impact.
        </p>

        <p style='font-size: 20px; text-align: justify; line-height: 1.6;'>
        The consequences of terrorism include humanitarian crises, economic disruptions, and political instability. Governments and 
        international bodies like the UN and NATO work to counteract threats through intelligence sharing, financial sanctions, 
        and counter-radicalization programs. Addressing the root causes remains key to long-term solutions.
        </p>
        """, unsafe_allow_html=True)


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

        st.markdown(f"🛑 Total Incidents: {incidents:,}")
        st.markdown(f"🔥 Most Common Attack Type: {most_common_attack}")
    else:
        st.warning("No data available for the selected country.")

    st.markdown("---")  # Divider


elif page == "EDA":

     if "show_eda" not in st.session_state:
        st.session_state.show_eda = False

     if not st.session_state.show_eda:
        st.markdown("""
        <h1 style='text-align: center; color: #3366CC;'>🔍 Exploratory Data Analysis (EDA)</h1>
        <p style='text-align: center; font-size:18px;'>
            Welcome to the **Exploratory Data Analysis Dashboard**!  
            In this section, we take a deep dive into the **Global Terrorism Index 2023** dataset to uncover key insights.  
            Through interactive visualizations and statistical analysis, we aim to answer crucial questions, such as:
        </p>
        <ul>
            <li>📌 Which countries experience the highest number of terrorist incidents?</li>
            <li>📈 How have terrorist incidents, fatalities, and injuries evolved over time?</li>
            <li>🔥 What factors are most correlated with terrorism severity?</li>
            <li>🌍 How do terrorist incidents vary across different regions, and which areas are most affected?</li>
        </ul>
        <p style='text-align: center;'>Understanding these patterns is essential for policymakers, security agencies, and researchers working towards a safer world.</p>
        <hr style='border: 1px solid #ddd;'>
        <p style='text-align: center; font-size:16px; color:gray;'>
            👉 Click <b>'Explore Data 🔍'</b> to explore the data.
        </p>
        """, unsafe_allow_html=True)
       
        image = Image.open("11.webp")  
        st.image(image, use_container_width=True)

         
        if st.button("Explore Data 🔍"):
           st.session_state.show_eda = True
           st.query_params["scroll"] = "top"
           st.rerun()
            
     else:
      query_params = st.query_params  
      if "scroll" in query_params and query_params["scroll"] == "top":
            st.markdown("""
                <script>
                    window.scrollTo(0, 0);
                </script>
            """, unsafe_allow_html=True)
            st.query_params.clear()
      tab1, tab2, tab3, tab4 = st.tabs(["🌍 Geographic Analysis", "📌 Top 10 Countries", "📈 Global Terrorism Trends Over the Years","🔥 Terrorism Score vs Severity"])
     
   
      with tab2:
         st.markdown("## 📌 Top 10 Most Affected Countries")
        
        # Aggregating data to find top affected countries
         country_counts = data.groupby("Country")["Incidents"].sum().reset_index()
         top_countries = country_counts.sort_values(by="Incidents", ascending=False).head(10)

         fig = px.bar(
            top_countries,
            x="Country",
            y="Incidents",
            color="Incidents",
            color_continuous_scale="Reds",
            text="Incidents",
            title="Top 10 Countries with Highest Terrorism Incidents"
        )
         fig.update_traces(textposition="outside")
         fig.update_layout(
            xaxis_title="Country",
            yaxis_title="Number of Incidents",
            coloraxis_showscale=False,
            uniformtext_minsize=8,
            uniformtext_mode='hide'
         )

         st.plotly_chart(fig, use_container_width=True)
    

        # Data Table
         st.subheader("Top 10 Countries Data")
         st.write(top_countries)


         st.markdown("""
           <h2 style='text-align: center;'>Global Terrorism Impact: Top 10 Most Affected Countries</h2>
           <p style='font-size:18px;'>
           This visualization presents the top 10 countries most affected by terrorism, combining bar charts and data tables. plots to provide a comprehensive view of terrorism incidents worldwide.  
           The data clearly illustrates the unequal distribution of terrorist attacks, with some nations experiencing significantly higher numbers of incidents compared to others.
           </p>

           <p style='font-size:18px;'>
           From the data, it is evident that Iraq, Afghanistan, Pakistan, and Somalia bear the highest burden of terrorist activities, with incident numbers far exceeding those in other regions.  
           A sharp decline in incidents is observed from India onwards, indicating that the impact of terrorism is not evenly distributed geographically but rather concentrated in specific regions.  
           Certain countries are significantly more vulnerable to attacks compared to others, emphasizing the need for targeted security measures and geopolitical analysis.
           </p>
           """, unsafe_allow_html=True)



    # 📈 Global Terrorism Trends Over the Years
      with tab3:
         st.markdown("## 📈 Global Terrorism Trends Over the Years")

   
         file_path = "Global Terrorism Index 2023.csv"
         df = pd.read_csv(file_path)

    
         global_trend = df.groupby("Year").agg({
             "Hostages": "sum",
             "Fatalities": "sum",
             "Injuries": "sum"
         }).reset_index()

    
         st.write("### Yearly Aggregated Data")
         st.dataframe(global_trend) 

        
         df_melted = global_trend.melt(id_vars="Year", 
                                  value_vars=["Hostages", "Fatalities", "Injuries"],
                                  var_name="Type", value_name="Count")

         fig = px.line(df_melted, x="Year", y="Count", color="Type",
                  markers=True,
                  line_dash="Type",  
                  title="Global Terrorism Trends: Hostages, Fatalities, Injuries",
                  color_discrete_map={
                      "Hostages": "green",
                      "Fatalities": "orange",
                      "Injuries": "royalblue"
                  })

         fig.update_traces(mode="lines+markers")
         
         fig.update_layout(
            legend_title_text="Category",
            hovermode="x unified",
            xaxis_title="Year",
            yaxis_title="People Count",
            yaxis_tickformat=",",  
            template="simple_white",
            xaxis=dict(
                showgrid=True,
                gridcolor='lightgrey',
                gridwidth=1
             ),
            yaxis=dict(
                showgrid=True,
                gridcolor='lightgrey',
                gridwidth=1
             )
         )
          
         st.plotly_chart(fig, use_container_width=True)
         

         st.markdown("""
           <h2 style='text-align: center;'>Global Terrorism Trends (2012-2022)</h2>
           <p style='font-size:18px;'>
           This line chart illustrates the trends in global terrorist incident hostages（Total Hostages）, fatalities (Total Fatalities), and injuries (Total Injuries) from 2012 to 2022. 
           </p>

           <p style='font-size:18px;'>
           From the chart, it is evident that the total number of hostages (green) has remained relatively stable, But after a sharp surge to a decade-high in 2018-2020, it fell sharply. This may be due to some large events. For example, the rise may be due to a concentration of high-impact kidnappings in conflict-prone areas such as Nigeria or Afghanistan. Then it fell sharply due to the global damage caused by the COVID-19 pandemic.
           
           Fatalities (orange) peaked between 2014 and 2016 but have gradually declined, suggesting that the lethality of attacks has decreased over time.  
 
           Injuries (blue) fluctuated significantly between 2012 and 2017 but showed an overall downward trend afterward, indicating that while the impact of terrorist attacks varied, their overall destructive capacity has diminished, potentially due to changes in attack methods.  

           Despite the decline in casualties, terrorism remains a global security threat, necessitating continuous monitoring and preventive measures.
           </p>
          """, unsafe_allow_html=True)

    #🔥 Terrorism Score vs Severity
      with tab4:
         st.markdown("## 🔥 Correlation Heatmap: Terrorism Score vs Severity")
         st.write("This heatmap visualizes the correlation between terrorism scores, attack incidents, fatalities, injuries, and hostage situations.")

         selected_columns = ['Score', 'Incidents', 'Fatalities', 'Injuries', 'Hostages']
         correlation_matrix = df[selected_columns].corr().round(2)

         fig = px.imshow(
           correlation_matrix,
           text_auto=True, 
           color_continuous_scale="RdBu_r",  
           zmin=-1,
           zmax=1,
           aspect="auto",
           title=" 🔥 Correlation Heatmap: Terrorism Score vs Severity"
       )

         fig.data[0].colorbar.title = dict(text="Correlation", font=dict(size=10))
         fig.data[0].colorbar.tickfont = dict(size=10)

         fig.update_layout(
            width=450,  
            height=400,
            margin=dict(l=10, r=10, t=50, b=10)
       )

         st.plotly_chart(fig, use_container_width=True)
         
         
         st.markdown("""
           <h2 style='text-align: center;'> Insights from the Correlation Heatmap</h2>

           <p style='font-size:18px;'>
           From the heatmap, we can observe the following trends:
           </p>

           <ul style='font-size:18px;'>
           <li><b>Terrorism Score (Score)</b> and <b>Terrorist Incidents (Incidents)</b> have a correlation of <b>0.52</b>, indicating that countries with higher scores tend to experience more terrorist attacks. However, the correlation is not very strong, suggesting that the score may also be influenced by other factors.</li>

           <li><b>Terrorist Incidents (Incidents)</b> are highly correlated with <b>Fatalities (Fatalities)</b> and <b>Injuries (Injuries)</b>, meaning that more attacks generally result in higher casualties.</li>

           <li><b>Fatalities (Fatalities)</b> and <b>Injuries (Injuries)</b> have a correlation of <b>0.91</b>, suggesting that a single terrorist attack often results in both deaths and injuries.</li>

           <li><b>Hostage Numbers (Hostages)</b> show lower correlation with other variables (maximum <b>0.32</b>), indicating that hostage-taking incidents may not be directly related to general terrorist attacks or their casualties, and might involve different attack patterns.</li>
           </ul>

           <p style='font-size:18px;'>
           This analysis provides a quantitative view of how different terrorism-related factors interact, helping policymakers and researchers understand the broader impact of terrorist activities.
           </p>
           """, unsafe_allow_html=True)
          
        
    # 🌍 Geographic Analysis
      with tab1:
         st.markdown("## 🌍 Global Terrorism Incidents by Country")
         st.write("This map visualizes the distribution of terrorist incidents around the world based on the frequency of attacks.")
         
         df_geo = df[['Country', 'Incidents']].groupby('Country').sum().reset_index()


         country_corrections = {
         "United States of America": "United States",
         "Cote d' Ivoire": "Ivory Coast",
         "Democratic Republic of the Congo": "Congo (Kinshasa)",
         "Republic of the Congo": "Congo (Brazzaville)"
        }
         df_geo["Country"] = df_geo["Country"].replace(country_corrections)

         df_geo["Incidents"] = pd.to_numeric(df_geo["Incidents"], errors="coerce").fillna(0)
        
         fig = px.choropleth(
            df_geo,
            locations="Country",
            locationmode="country names",
            color="Incidents",
            hover_name="Country",
            hover_data=["Incidents"],
            color_continuous_scale="Reds",
            title="Global Distribution of Terrorist Incidents",
            range_color=(0, df_geo['Incidents'].max())  
        )
         st.plotly_chart(fig, use_container_width=True)

         st.markdown("""
             <h3 style='text-align: center;'> Global Terrorism Incident Distribution</h3>

             <p style='font-size:18px;'>
             This map reveals that <b>Iraq</b> is the country most severely affected by terrorism, with the highest number of incidents.  
             Countries in <b>South Asia</b>, such as <b>Pakistan</b> and <b>India</b>, as well as <b>Middle Eastern nations</b> like <b>Syria</b> and <b>Afghanistan</b>, exhibit a high frequency of terrorist attacks, indicating that these regions remain major hotspots for terrorism.  
             </p>

             <p style='font-size:18px;'>
             Compared to the Middle East and South Asia, <b>Africa</b> has relatively fewer terrorist incidents, but countries such as <b>Somalia, Nigeria, and Burkina Faso</b> still experience a significant level of terrorist activity, as indicated by the darker colors on the map.  
             </p>

             <p style='font-size:18px;'>
             Most <b>Western countries</b> (such as the <b>United States, Canada, Australia, and European nations</b>) appear in lighter shades, suggesting fewer terrorist incidents. This may indicate more effective security controls and counter-terrorism measures in these countries.
             </p>

             <p style='font-size:18px; font-weight: bold;'>
             These trends highlight the importance of the global fight against terrorism, particularly the need to strengthen security measures and international cooperation in conflict-prone regions to reduce the threat of terrorism.
             </p>
             """, unsafe_allow_html=True)


if page == "Prediction":
    sns.set_style("whitegrid")
    sns.set_palette("Set2")
    
    # Title for the Prediction Page
    st.markdown("<p class='title'> Terrorism Incident Prediction</p>", unsafe_allow_html=True)
    st.write("""
    This application predicts future terrorism incidents using *SARIMA (Seasonal ARIMA)*, 
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
    fig_top5.add_trace(go.Bar(
        x=top_countries["Incidents"],
        y=top_countries["Country"],
        orientation="h",
        marker=dict(color=top_countries["Incidents"], colorscale="Reds"),
        text=top_countries["Incidents"],
        textposition="outside",
    ))
    fig_top5.update_layout(
        title="Top 5 Countries with the Most Terrorism Incidents",
        xaxis_title="Total Incidents",
        yaxis_title="Country",
        font=dict(size=14, family="Arial, sans-serif"),
        template="plotly_white",
        margin=dict(l=100, r=50, t=80, b=50),
        hovermode="y unified",
    )
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
        st.warning(f"No data available for {selected_country}. Unable to make predictions.")
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
            fig.add_trace(go.Scatter(
                x=incidents_by_year["Year"],
                y=incidents_by_year["Incidents"],
                mode="lines+markers",
                name="Actual Data",
                line=dict(color="#4C72B0", width=2),
                marker=dict(size=8)
            ))
            fig.add_trace(go.Scatter(
                x=forecast_years,
                y=forecast_values,
                mode="lines+markers",
                name="Forecast",
                line=dict(color="green", width=2, dash="dash"),
                marker=dict(size=8)
            ))
            fig.update_layout(
                title=f"Incident Prediction for {selected_country}",
                xaxis_title="Year",
                yaxis_title="Total Incidents",
                font=dict(size=14, family="Arial, sans-serif"),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                hovermode="x unified",
                template="plotly_white",
                margin=dict(l=50, r=50, t=80, b=50)
            )
            
            # Add explanatory text above the graph
            st.subheader("Incident Prediction Graph")
            st.write("""
            The graph below shows the historical and predicted terrorism incidents for the selected country. 
            - *Blue Line*: Represents the actual number of incidents recorded in previous years.
            - *Green Dashed Line*: Represents the forecasted number of incidents for future years.
            - Hover over the data points to see exact values for each year.
            Note: The predictions are based on the SARIMA model and may not account for unforeseen events or changes in trends.
            """)
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
            st.write(f"- *Mean Absolute Error (MAE)*: {mae:.2f}")
            st.write(f"- *Root Mean Squared Error (RMSE)*: {rmse:.2f}")
