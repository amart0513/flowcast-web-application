import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

IMAGE_FIU_BANNER = "media/FIU_Banner.png"
API_URL = "https://www.ndbc.noaa.gov/data/realtime2/<station_id>.txt"

st.set_page_config(page_title="FlowCast: NOAA Data", layout="wide", page_icon="🌊", initial_sidebar_state="expanded")

# Custom CSS for consistent banner and optimized layout
st.markdown(
    """
    <style>
        /* Consistent Banner */
        .hero-title {
            font-size: 3rem;
            font-weight: bold;
            color: white;
            text-align: center;
            background: linear-gradient(135deg, #005f73, #0a9396);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 10px; /* Reduced margin */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        /* Consistent Subtitle and Subheader Styles */
        .styled-subheader {
            font-size: 1.5rem;
            font-weight: bold;
            color: #005f73; /* Same color as the banner */
            margin: 5px 0; /* Reduced vertical spacing */
        }

        /* Section Container */
        .section-container {
            padding: 20px 50px;
            font-family: 'Arial', sans-serif;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px; /* Reduced margin */
        }

        /* Divider Style */
        .divider {
            border-top: 2px solid #005f73;
            margin: 10px 0; /* Reduced margin */
        }

        /* Center Text */
        .center-text {
            text-align: center;
            margin: 0; /* Removed extra margins */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Consistent banner
st.markdown('<div class="hero-title">Real-Time Data from NOAA</div>', unsafe_allow_html=True)


# Function to display raw data
def raw_data(df):
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="styled-subheader">Fetched Data</div>', unsafe_allow_html=True)
    st.dataframe(df)
    st.markdown('<div class="styled-subheader">Descriptive Statistics</div>', unsafe_allow_html=True)
    st.dataframe(df.describe())
    st.markdown('</div>', unsafe_allow_html=True)


# Function to render data from NOAA API
def render_API():
    # Sidebar for station selection
    stations = {
        '41122': 'Hollywood Beach, FL',
        '41114': 'Fort Pierce, FL',
        '41010': 'Cape Canaveral, FL',
        '42036': 'Tampa, FL',
        '41070': 'Daytona Beach, FL'
    }

    selected_station = st.sidebar.selectbox("Select a Station", list(stations.values()))
    station_id = [k for k, v in stations.items() if v == selected_station][0]

    response = requests.get(API_URL.replace('<station_id>', station_id))
    if response.status_code == 200:
        data = response.text.splitlines()
        columns = ['YY', 'MM', 'DD', 'hh', 'mm', 'WDIR', 'WSPD', 'GST', 'WVHT', 'DPD', 'APD', 'MWD',
                   'PRES', 'ATMP', 'WTMP', 'DEWP', 'VIS', 'PTDY', 'TIDE']

        # Create the DataFrame
        df_api = pd.DataFrame([x.split() for x in data[2:] if x.strip() != ''], columns=columns)

        # Convert WTMP to numeric, forcing errors to NaN
        df_api['WTMP'] = pd.to_numeric(df_api['WTMP'], errors='coerce')

        # Station Title
        st.markdown(f'<h3 class="center-text styled-subheader">{selected_station}</h3>', unsafe_allow_html=True)

        # Display raw data
        raw_data(df_api)

        # Check for valid data in WTMP
        valid_data = df_api['WTMP'].dropna()
        if not valid_data.empty:
            # Create a line chart using matplotlib
            st.markdown('<div class="section-container">', unsafe_allow_html=True)
            st.markdown(f'<div class="styled-subheader">Water Temperature at {selected_station}</div>',
                        unsafe_allow_html=True)
            plt.figure(figsize=(10, 5))
            plt.plot(valid_data.index, valid_data, marker='o', linestyle='-', color='b')
            plt.title(f"Water Temperature at {selected_station}", fontsize=16)
            plt.xlabel("Data Points", fontsize=12)
            plt.ylabel("Water Temperature (°C)", fontsize=12)
            plt.xticks(rotation=45, fontsize=10)
            plt.grid()
            plt.tight_layout()
            st.pyplot(plt)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning(f"No valid water temperature data available for {selected_station}.")
    else:
        st.error(f"Failed to retrieve data for station ID {station_id}. Please try again.")


# Call render_API to display the page
render_API()
