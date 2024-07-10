# Fish Data Visualization

## Overview

This application visualizes fish data from the game Stardew Valley. It allows users to filter fish based on various criteria, adjust price modifiers, and view the results in an interactive bar chart.

## Features

- **Filtering Options**: Filter fish by name, location, time of day, season, and weather conditions.
- **Exclusivity Filters**: Option to apply exclusive filters for locations, times of day, seasons, and weather conditions.
- **Exclude Fish Categories**: Exclude Night Market, Legendary, and Legendary II fish categories with checkboxes checked by default.
- **Price Modifiers**: Adjust fish prices based on quality and profession modifiers.
- **Interactive Bar Chart**: View average fish prices in an interactive Plotly bar chart with hover-over tooltips displaying integer prices.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/fish-data-visualization.git
   cd FishData
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Ensure your fish data CSV file is in the same directory as the `FishData.py` script and named `fish_data.csv`.

## Usage

1. Run the Streamlit application:

   ```sh
   streamlit run FishData.py
   ```

2. Open your web browser and go to the URL provided by Streamlit to interact with the application.

## File Structure

- `FishData.py`: Main script for the Streamlit application.
- `fish_data.csv`: CSV file containing the fish data.
- `requirements.txt`: List of required Python packages.

## Data Format

The `fish_data.csv` file should have the following columns:

- `name`: Name of the fish.
- `price`: Base price of the fish.
- `type`: Category of the fish (e.g., common, night market, legendary, legendary II).
- `ocean`, `river`, `pond`, `lake`, `waterfall`, `woods`, `sewer`, `swamp`, `mines`, `desert`, `mutant bug lair`, `cove`, `ginger ocean`, `ginger pond`, `ginger river`, `volcano`, `night market`: Boolean columns indicating where the fish can be found.
- `morning`, `afternoon`, `evening`, `night`: Boolean columns indicating when the fish can be caught.
- `spring`, `summer`, `fall`, `winter`: Boolean columns indicating the seasons when the fish can be caught.
- `sun`, `rain`, `wind`: Boolean columns indicating the weather conditions under which the fish can be caught.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
