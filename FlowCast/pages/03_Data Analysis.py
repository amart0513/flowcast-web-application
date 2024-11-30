import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="FlowCast: Data Analysis", layout="wide", page_icon="🌊")

# Custom CSS for Consistent Banner, Subtitles
st.markdown(
    """
    <style>
        /* Banner Styling */
        .hero-title {
            font-size: 3rem;
            font-weight: bold;
            color: white;
            text-align: center;
            background: linear-gradient(135deg, #005f73, #0a9396);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        /* Section Container */
        .section-container {
            padding: 20px 50px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Styled Subheaders and Subtitles */
        .styled-subheader {
            font-size: 1.5rem;
            font-weight: bold;
            color: #005f73; /* Banner Consistent Color */
            margin-bottom: 15px;
        }

        /* Tooltip Styling */
        .tooltip {
            font-size: 0.9rem;
            color: gray;
        }

        /* Metric Box */
        .metric-box {
            background-color: #f7f9fa;
            border: 1px solid #e3e6e8;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 15px;
            text-align: center;
        }

        /* Divider */
        .divider {
            border-top: 2px solid #005f73;
            margin: 30px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Banner Title
st.markdown('<div class="hero-title">Data Analysis</div>', unsafe_allow_html=True)

# Function to Render Data
def render_data():
    # Toggle for Dataset Selection
    dataset_toggle = st.radio("Choose Dataset", ["Default Dataset", "Upload Your Own"], help="Select a dataset to analyze.")

    # File Upload Section
    if dataset_toggle == "Upload Your Own":
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully.")
        else:
            st.warning("Please upload a CSV file to proceed.")
            return
    else:
        df = pd.read_csv("oct25-2024.csv")
        st.info("Using the default dataset.")

    # Validate Data
    required_columns = ['Depth m', 'Temp °C', 'pH', 'ODO mg/L']
    for column in required_columns:
        if column not in df.columns:
            st.error(f"Missing column: {column}. Please upload a valid CSV file.")
            return

    if df.isnull().values.any():
        st.warning("Data contains NaN values. Please clean your data.")

    # Data Analysis Section
    st.markdown('<div class="section-container">', unsafe_allow_html=True)

    # Sliders for Filtering
    st.markdown('<div class="slider-container">', unsafe_allow_html=True)
    st.markdown('<p class="styled-subheader">Filter Data</p>', unsafe_allow_html=True)

    min_depth, max_depth = df["Depth m"].min(), df["Depth m"].max()
    min_temp, max_temp = df["Temp °C"].min(), df["Temp °C"].max()
    min_ph, max_ph = df["pH"].min(), df["pH"].max()

    selected_depth = st.slider("Select Depth (m)", min_value=min_depth, max_value=max_depth,
                               value=(min_depth, max_depth))
    selected_temp = st.slider("Select Temperature (°C)", min_value=min_temp, max_value=max_temp,
                              value=(min_temp, max_temp))
    selected_ph = st.slider("Select pH", min_value=min_ph, max_value=max_ph, value=(min_ph, max_ph))
    st.markdown('<p class="tooltip">Use the sliders to filter data points based on your selection.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Filter Data
    filtered_df = df[(df["Depth m"].between(selected_depth[0], selected_depth[1])) &
                     (df["Temp °C"].between(selected_temp[0], selected_temp[1])) &
                     (df["pH"].between(selected_ph[0], selected_ph[1]))]

    st.metric(label="Filtered Data Points", value=len(filtered_df))

    # Visualization Tabs
    Scatter_Plots_tab, Maps_tab, Line_Plots_tab, threeD_Plots_tab, Raw_Plots_tab = st.tabs(
        ["Scatter Plots", "Maps", "Line", "3D Plots", "Raw Data"])

    with Scatter_Plots_tab:
        st.markdown('<p class="styled-subheader">Scatter Plot</p>', unsafe_allow_html=True)
        fig = px.scatter(filtered_df, x="Depth m", y="Temp °C", size="pH", color="ODO mg/L")
        st.plotly_chart(fig)

    with Maps_tab:
        st.markdown('<p class="styled-subheader">Maps</p>', unsafe_allow_html=True)
        if 'Latitude' in df.columns and 'Longitude' in df.columns:
            fig = px.scatter_mapbox(filtered_df, lat="Latitude", lon="Longitude",
                                    hover_data=["Depth m", "pH", "Temp °C", "ODO mg/L"],
                                    zoom=15)
            fig.update_layout(mapbox_style="open-street-map")
            st.plotly_chart(fig)
        else:
            st.error("Missing 'Latitude' or 'Longitude' columns in data.")

    with Line_Plots_tab:
        st.markdown('<p class="styled-subheader">Line Plot</p>', unsafe_allow_html=True)
        color = st.color_picker("Choose a color", "#081E3F")
        fig = px.line(filtered_df, x=filtered_df.index, y="ODO mg/L")
        fig.update_traces(line_color=color)
        st.plotly_chart(fig)

    with threeD_Plots_tab:
        st.markdown('<p class="styled-subheader">3D Plot</p>', unsafe_allow_html=True)
        fig = px.scatter_3d(filtered_df, x="Longitude", y="Latitude", z="Depth m", color="ODO mg/L")
        fig.update_scenes(zaxis_autorange="reversed")
        st.plotly_chart(fig)

    with Raw_Plots_tab:
        st.markdown('<p class="styled-subheader">Fetched Data</p>', unsafe_allow_html=True)
        st.dataframe(filtered_df)
        st.markdown('<p class="styled-subheader">Descriptive Statistics</p>', unsafe_allow_html=True)
        st.dataframe(filtered_df.describe())

    st.markdown('</div>', unsafe_allow_html=True)


render_data()
