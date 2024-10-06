# Air Quality Data Analysis Dashboard 🌿💨

This project is a **data analysis dashboard** that visualizes air quality data from various monitoring stations. It provides insights into the spatial and temporal patterns of pollutants, compares pollution levels between weekdays and weekends, and explores the impact of wind speed on pollutant dispersion.

The dashboard is built using **Streamlit**, **Pandas**, **Seaborn**, and **Matplotlib** to create interactive visualizations of the air quality data.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Run the Dashboard](#how-to-run-the-dashboard)
5. [Dataset](#dataset)
6. [Visualizations](#visualizations)
7. [Conclusion](#conclusion)
8. [Contact](#contact)

## Project Overview
This dashboard helps analyze air quality by visualizing different pollutants (PM2.5, PM10, NO2, SO2, CO, and O3) collected from various monitoring stations. The project explores patterns in pollution based on location, compares pollution levels between weekdays and weekends, and investigates the effect of wind speed on pollutant concentration.

The analysis provides actionable insights into the quality of air in different regions and how environmental factors such as wind speed influence the spread of pollutants.

**You can access the live dashboard here: [Air Quality Dashboard on Streamlit Cloud](https://airquality-ai.streamlit.app/)**.

## Features
- **Pollutant Visualization by Location:** Shows air quality across different monitoring stations.
- **Weekdays vs. Weekends Comparison:** Compares pollution levels on weekdays and weekends.
- **Wind Speed Impact:** Explores how wind speed affects pollutant concentration.
- **Interactive Dashboard:** Easy-to-use interface built with Streamlit for exploring the data and visualizations.

## Installation
Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.8 or higher
- `pip` for package management
- Internet connection to download dependencies

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/air-quality-dashboard.git
   cd air-quality-dashboard
2. **Create a virtual environment**(optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
4. **Download the dataset:**
    Ensure the main dataset (main_data.csv) is placed in the dashboard directory of the project.

## How to Run the Dashboard
Once you have installed the required dependencies, you can run the dashboard locally by following these steps:

1. **Access data on dashboard directory**
    ```bash
    cd dashboard
2. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
3. **Access the dashboard:**
    After running the above command, Streamlit will launch a local web server. You can view the dashboard in your browser at:
    ```bash
    http://localhost:8501

Or visit the deployed version at https://airquality-ai.streamlit.app/.

## Dataset
The dataset used in this project includes daily measurements of air pollutants collected from various air quality monitoring stations. The key columns include:

- `PM2.5`, `PM10`, `NO2`, `SO2`, `CO`, `O3` - pollutant concentrations (μg/m³)
- `station` - the location of the monitoring station
- `year`, `month`, `day` - date of the recorded data
- `WSPM` - wind speed (m/s)

The dataset is used to answer questions about spatial, temporal, and environmental influences on air quality.

## Visualizations

### 1. Pollutant Visualization by Location 🌍

Displays the concentration of various pollutants at different monitoring stations.

### 2. Weekdays vs. Weekends 📅

Compares air pollution levels between weekdays and weekends to identify differences in pollution patterns based on human activity.

### 3. Wind Speed Impact 🌬️

Shows the relationship between wind speed and pollutant concentrations, visualizing how higher wind speeds can disperse pollutants.

## Conclusion

This project provides meaningful insights into air quality based on location, time, and meteorological factors. By visualizing the data, we can better understand how human activity and natural conditions influence pollution levels.

## Contact

For any questions or feedback, feel free to reach out to:

**Author:** Aini Azzah

**Email:** ainiazzah22@gmail.com

**ID Dicoding:** Aini Azzah