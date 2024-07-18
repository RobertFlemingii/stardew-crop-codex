Stardew Valley Data Visualization
Overview
This application provides interactive data visualization for various aspects of Stardew Valley gameplay. The app features different sections for fishing, foraging, mining, ranching, and tilling, each with its own set of filters and visualizations.

Features
Fishing: Visualize and filter fish data by name, location, time of day, season, and weather conditions. View average fish prices with interactive charts.
Foraging: Analyze foraging data with various filters and visualizations.
Mining: Explore mining data and visualizations.
Ranching: View and filter ranching data.
Tilling: Analyze tilling data with interactive visualizations.
Navigation: Navigate between different sections using a taskbar and a main menu with clickable icons.
File Structure
assets/: Folder for asset files (currently not in use)
fish_sprites/: Folder for fish sprites (currently not in use)
icons/: Contains icon images for navigation buttons
app.py: Main script for running the Streamlit application
artisan_goods.py: Script related to artisan goods data
fish_data.csv: CSV file containing fish data
fishing.py: Script for fishing data and visualization
foraging.py: Script for foraging data and visualization
foraging_data.csv: CSV file containing foraging data
mine_data.csv: CSV file containing mining data
mining.py: Script for mining data and visualization
ranching.py: Script for ranching data and visualization
ranching_data.csv: CSV file containing ranching data
requirements.txt: List of required Python packages
tilling.py: Script for tilling data and visualization
tilling_data.csv: CSV file containing tilling data
Installation
Clone the Repository

sh
Copy code
git clone https://github.com/yourusername/stardew-valley-data-visualization.git
cd stardew-valley-data-visualization
Install Dependencies

sh
Copy code
pip install -r requirements.txt
Prepare Data Files

Ensure the required CSV files (fish_data.csv, foraging_data.csv, mine_data.csv, ranching_data.csv, tilling_data.csv) are present in the project directory.

Usage
Run the Application

sh
Copy code
streamlit run app.py
Open the Web Application

Open your web browser and go to the URL provided by Streamlit to interact with the application.

Development
To make updates or contribute to the project:

Update Scripts: Modify the scripts for different sections (e.g., fishing.py, foraging.py, etc.) to add or change functionalities.
Add Data Files: Place new data files in the project directory and ensure they are referenced correctly in the scripts.
Icons and Assets: Place any new icons or assets in the icons/ and assets/ folders as needed.
