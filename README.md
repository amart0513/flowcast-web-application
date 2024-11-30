# FlowCast: Real-Time Water Monitoring and Prediction

## Overview

This project is a water quality predictor built using Python, HTML, CSS, JavaScript, and Streamlit, an open-source Python library for creating web apps, and powered by machine learning for water quality prediction. The app focuses on predicting water quality in specific regions, such as Biscayne Bay and Haulover Beach, while visualizing and analyzing historical and real-time water quality data.

## Features

- [X] Real-time Data Integration: Fetches live water quality data from the NOAA API for continuous updates.
- [X] Interactive Visualizations: Visualize water quality data through scatter plots, line charts, maps, and 3D plots.
- [X] Machine Learning Predictions: Predict water quality parameters (e.g., oxygen levels, temperature) based on historical trends.
- [X] Multiple Station Analysis: Compare data across different water stations by selecting multiple station IDs for side-by-side charts and visualizations.
- [X] User Engagement: Users can upload their own water quality data, view past research summaries, and sign up for updates.

## Table of Contents

1. Installation
2. How It Works
3. Data Sources
4. Machine Learning Model
5. Usage
6. Features
7. Contributing
8. License

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

git clone https://github.com/your-username/water-quality-predictor.git
cd water-quality-predictor

2. Install the required dependencies:

pip install -r requirements.txt

3. Run the Streamlit app:

streamlit run app.py

## How It Works

The app collects real-time data from various water monitoring stations using the NOAA API. The machine learning model processes this data to predict water quality metrics, such as oxygen concentration, temperature, and pH. Users can visualize these metrics through dynamic charts and graphs and compare them across multiple monitoring stations.

Key technologies used:

- Streamlit: For building the web interface.
- Scikit-learn: For training and using machine learning models.
- Pandas & NumPy: For data manipulation.
- Matplotlib & Plotly: For visualizations.
- NOAA API: For real-time data integration.

## Data Sources

We utilize historical and real-time water quality data from various sources:

- NOAA (National Oceanic and Atmospheric Administration): For real-time and historical water quality data.
- User-Uploaded Data: Users can upload CSV files with water quality data to compare against existing records.

## Machine Learning Model

The machine learning model is trained to predict water quality parameters like dissolved oxygen (DO), pH, and temperature. The training data includes historical records from water monitoring stations in Biscayne Bay and Haulover Beach.

Key steps in model development:

1. Data Preprocessing: Cleaning and normalizing the data.
2. Feature Engineering: Selecting relevant features like water temperature, salinity, and depth.
3. Model Training: Training using models like Random Forest, SVM, or Gradient Boosting.
4. Model Evaluation: Evaluating the model’s accuracy and performance with test data.

## Usage

1. Select Water Station IDs: Choose one or more station IDs to visualize water quality data.
2. View Predictions: The machine learning model predicts water quality metrics based on selected parameters.
3. Upload Data: Users can upload their own data for comparison and analysis.
4. Visualize: The app displays dynamic charts and tables for easy interpretation.

## Features

1. Water Quality Prediction: Predict key metrics like temperature, pH, and dissolved oxygen.
2. Historical Data Analysis: Explore past trends in water quality data across multiple regions.
3. Custom Data Uploads: Upload your own data to run custom analysis and predictions.
4. Interactive Visualizations: Use scatter plots, line charts, maps, and 3D visualizations to better understand the data.

## Contributing

We welcome contributions! If you’d like to help improve this project, feel free to:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -m 'Add your feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
