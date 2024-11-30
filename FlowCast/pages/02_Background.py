import streamlit as st

IMAGE1 = "media/boat1.jpg"
IMAGE2 = "media/boat2.jpg"
IMAGE_FIU_BANNER = "media/FIU_Banner.png"

st.set_page_config(page_title="FlowCast", layout="wide",
                   page_icon="🌊", initial_sidebar_state="expanded")

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* General Styles */
        .main-container {
            font-family: 'Arial', sans-serif;
            padding: 20px 50px;
        }
        .hero-title {
            font-size: 2.8rem;
            font-weight: bold;
            color: white;
            text-align: center;
            background: linear-gradient(135deg, #005f73, #0a9396);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .section-header {
            font-size: 2.5rem;
            text-align: center;
            margin-top: 40px;
            margin-bottom: 20px;
            color: #005f73;
        }
        .divider {
            border: 0;
            height: 1px;
            background: linear-gradient(to right, #005f73, #0a9396, #005f73);
            margin: 30px 0;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .card img {
            border-radius: 10px;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        .card img:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .rounded-image {
            border-radius: 10px;
        }
        .back-to-top {
            text-align: center;
            margin-top: 30px;
        }
        .back-to-top a {
            text-decoration: none;
            font-size: 1.2rem;
            color: #0a9396;
            font-weight: bold;
        }
        .back-to-top a:hover {
            color: #005f73;
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Custom CSS with Lighter Blue Background
st.markdown(
    """
    <style>
        /* Sidebar container */
        [data-testid="stSidebar"] {
            background-color: #b3dfe6; /* Lighter blue background */
            color: white; /* Default text color */
            padding: 20px;
        }

        /* Sidebar title */
        [data-testid="stSidebar"] h1 {
            font-size: 1.5rem;
            color: #005f73; /* Darker blue for title */
            text-align: center;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Sidebar widget labels */
        [data-testid="stSidebar"] label {
            font-size: 1rem;
            color: #005f73; /* Darker blue for labels */
            margin-bottom: 8px;
        }

        /* Sidebar buttons */
        [data-testid="stSidebar"] button {
            background-color: #0a9396;
            color: white; /* Button text color */
            font-size: 1rem;
            border-radius: 8px;
            padding: 10px 15px;
            margin: 10px 0;
            border: none;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.3s;
        }

        [data-testid="stSidebar"] button:hover {
            background-color: white; /* Hover background */
            color: #005f73; /* Hover text color */
            transform: scale(1.05);
        }

        /* Sidebar dropdowns and sliders */
        [data-testid="stSidebar"] .stSelectbox,
        [data-testid="stSidebar"] .stSlider {
            background-color: rgba(255, 255, 255, 0.1);
            color: #005f73; /* Darker blue for dropdown text */
            border-radius: 8px;
            padding: 5px;
            margin: 10px 0;
        }

        /* Sidebar text input */
        [data-testid="stSidebar"] input {
            background-color: rgba(255, 255, 255, 0.1);
            color: #005f73; /* Input text color */
            border-radius: 5px;
            padding: 5px;
            margin-bottom: 10px;
        }

        /* Sidebar hover effects for links */
        [data-testid="stSidebar"] a {
            color: #005f73; /* Link text color */
            text-decoration: none;
            font-weight: bold;
        }

        [data-testid="stSidebar"] a:hover {
            color: #0a9396;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def render_background():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Styled Title Section
    st.markdown('<div class="hero-title">Background</div>', unsafe_allow_html=True)

    # About the Project Section
    st.markdown('<h2 class="section-header">About Our Project</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <p>
                Our project centered on the real-time analysis of water quality using advanced machine learning techniques,
                specifically tailored for the unique environmental conditions of Biscayne Bay and Haulover Beach. The core of our approach
                was the seamless integration of field data, collected directly from these two coastal locations, into our machine learning
                models. This data included key water quality parameters such as pH levels, temperature, salinity, turbidity, and the presence
                of harmful pollutants or bacteria.
                </p>
                <p>
                By focusing on location-specific datasets, we were able to train our machine learning algorithms on highly relevant
                and accurate information, which significantly improved the performance of our predictive models. The real-time aspect of the
                analysis meant that the system could continuously update its predictions as new data became available, allowing it to forecast
                future water quality conditions with remarkable precision.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.image(IMAGE1, caption="The Heron collecting water quality data.", use_container_width=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Data Collection Process Section
    st.markdown('<h2 class="section-header">Data Collection Process</h2>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            """
            <div class="card">
                <p>
                Throughout our expeditions, we utilized cutting-edge sensors and automated sampling systems to gather 
                a comprehensive dataset on key water quality parameters, including temperature, pH, dissolved oxygen, and nutrient concentrations.
                Each measurement was paired with precise GPS coordinates, ensuring that the data collected was both geospatially and
                temporally accurate. This granular dataset laid the foundation for our machine learning model, enabling us to analyze
                water quality patterns with fine detail and precision.
                </p>
                <p>
                To prepare the data for machine learning training, we performed a thorough cleaning and preprocessing step, removing
                any inconsistencies and outliers to ensure the integrity of the dataset. The processed data was then divided into training
                and testing sets, with the training set used to fit our machine learning model. We employed techniques like feature scaling,
                normalization, and cross-validation to optimize the model's performance and reduce potential biases.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.image(IMAGE2, caption="Our team preparing for data collection in Biscayne Bay.")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Insights Section
    st.markdown('<h2 class="section-header">Real-Time Insights</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
            <p>
            Real-time data from NOAA’s API was also integrated into the dataset, providing up-to-date environmental variables
            for continuous model refinement. Alongside the raw data, we documented geographical features, marine life, and human activities
            in the study areas through photographs and videos. These visuals not only enriched the understanding of water quality trends
            but also served as powerful tools for community engagement and awareness regarding conservation efforts.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


render_background()
