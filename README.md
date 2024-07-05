# Stardew Valley Fish Data Visualization App

This Streamlit app visualizes fish prices in Stardew Valley, allowing users to filter and compare various attributes such as price, location, time, season, and weather conditions. The data is sourced from a CSV file containing detailed information about different fish types found on https://stardewvalleywiki.com/Fish.

## Features

- **Display Raw Data**: View the raw fish data in a tabular format.
- **Filter by Attributes**: Use dropdown menus to filter fish by name, location, time of day, season, and weather conditions.
- **Bar Charts**: Visualize average prices and presence in various attributes using bar charts.
- **Searchable Dropdowns**: Easily search and select options from dropdown menus.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fish-data-visualization.git
   cd fish-data-visualization
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your `fish_data.csv` file in the project directory.

2. Run the Streamlit app:

   ```bash
   streamlit run FishData.py
   ```

3. Open your web browser and navigate to `http://localhost:8501`.

## File Structure

```plaintext
fish-data-visualization/
│
├── fish_data.csv        # CSV file containing fish data
├── app.py               # Main Streamlit app script
├── README.md            # This README file
└── requirements.txt     # List of required packages
```
