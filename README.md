# Ocean and Global Change Project: Impact of Sea Level Rise on Andaman

See the Report: 22110103_Final_Report.pdf

This Streamlit application simulates the impact of sea level rise on the Andaman and Nicobar Islands, specifically analysing the loss of land across different land-use types.

## Overview

The app provides interactive visualisations of how rising sea levels will affect various topographical zones across the islands from the year 2050 up to 2300. It evaluates these changes based on three different Representative Concentration Pathway (RCP) trajectories: RCP 2.6, RCP 4.5, and RCP 8.5.

## Features

* **Climate Model Selection:** Choose between RCP 2.6, RCP 4.5, and RCP 8.5 trajectories to see varying emission scenarios.
* **Temporal Analysis:** An interactive slider allows users to view projections for the years 2050, 2100, 2150, 2200, 2250, and 2300.
* **Land-Use Breakdown:** Displays the exact percentage of land lost for specific zones, including Settlement, Agricultural, Grassland, Mangrove, and Forest lands.
* **2D and 3D Visualisations:** Generates interactive 3D surface plots and 2D contour maps of the remaining "unsubmerged" land elevations using Plotly.



## Scientific Assumptions

The underlying simulation operates on a few key assumptions:

* The region experiences a decrease in land level due to Glacial Isostatic Adjustment (GIA) of roughly 1 mm, and a tectonic uplift of approximately 1 mm. The net influence is approximated in the simulation without precise, localized subduction modelling.


* The present-day land-use status remains constant through the year 2300.


* There is no accounting for future deforestation driven by agriculture or human settlements.



## Requirements

Ensure you have Python installed along with the following libraries:

```bash
pip install streamlit numpy pandas matplotlib plotly pillow

```

## Directory Setup

The application requires a large set of pre-processed segmented images and elevation maps. Ensure all corresponding `.png` files referenced in the code are present in the same root directory as your script.

* **Segmented Land Maps:** e.g., `Builtland_segmented_2050_RCP26.png`, `Cropland_segmented_2100_RCP85.png`
* **Elevation Maps:** e.g., `Elevation_2050_RCP26.png`, `Elevation_2300_RCP85.png`

## How to Run

1. Save the code as a Python script (e.g., `app.py`).
2. Open your terminal and navigate to the project directory.
3. Run the following command:

```bash
streamlit run app.py

```

## Dataset Credits

* **Mangrove Ecosystems:** Kolli et al., "Assessment of change in the extent of mangrove ecosystems using different spectral indices in Google Earth engine based on Random Forest Model".
* **Digital Elevation Model:** SRTM Dataset from OpenTopography.
* **GIA Trends:** NASA GRACE mission data.
