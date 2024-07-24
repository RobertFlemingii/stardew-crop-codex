# Stardew Valley Data Visualization App
## Introduction
I couldn't find a comprehensive way to see which Stardew Valley items are most profitable in each category without manually searching through the wiki. This app solves that problem by providing a data-driven visualization.
## Features
- **Dynamic Data Loading**: Uses pandas to read CSV files, making it easy to update data without hardcoding.
- **Modifiers**: Applies mathematical multipliers for quality and farmer profession modifiers using helper functions.
- **Accurate** Calculations: Ensures price calculations round down to the nearest gold (g), matching the game's mechanics.
- **Multi-topic Coverage**: Includes multiple categories such as fishing, tilling, ranching, mining, and foraging, accessible through a sidebar.
- **Interactive Data Visualization**: Utilizes Plotly for creating bar charts with hover-over tooltips.
## Navigation
To maintain good screen economy and provide easy access to different data categories, a sidebar with navigation buttons was implemented.
### Sidebar Navigation
- **Categories**: Main Menu, Tilling, Ranching, Mining, Foraging, Fishing
- **Navigation Function**: Ensures that both the page and sidebar update correctly when switching tabs.
## Filtering and Display Options
- **Filtering Options**: Initially used select boxes, later switched to multi-select options to allow multiple filters.
- **Exclusive Filters**: Checkbox option to switch between exclusive and non-exclusive filters for conditions like weather.
- **Wiki-like Display**: Selectbox and table display to present selected items similarly to the wiki.
## Data Visualization
- **Plotly Bar Chart**: Organizes data in ascending order with interactive hover-over tooltips displaying additional information.
## Bugs and Solutions
During the development, several bugs and challenges were encountered. Here are some notable ones and their resolutions:
- **Incorrect Profession Modifier in Fish Data**:
  - **Problem**: Incorrect application of profession modifiers.
  - **Solution**: Separated quality multipliers from profession modifiers and ensured accurate calculations.
- **Checkbox States Not Retained**:
  - **Problem**: Checkboxes did not retain default states.
  - **Solution**: Initialized checkboxes with default states and handled state changes correctly.
- **Dropdown Menu Implementation**:
  - **Problem**: Dropdown menus for quality and profession modifiers were confusing.
  - **Solution**: Used selectbox for single selections and ensured proper functionality through user feedback and testing.
- **Plotly Bar Chart Tooltips**:
  - **Problem**: Tooltips displayed float prices.
  - **Solution**: Rounded values to integers for clearer visualization.
- **Gold per Day (GPD) Calculation for Crops**:
  - **Problem**: Inconsistent GPD calculations in Google Sheets.
  - **Solution**: Standardized formulas for Seed Price, Sell Price, Yield, Grow Time, and Regrow Time.
- **CSV Data Integrity**:
  - **Problem**: Inconsistent data in CSV files.
  - **Solution**: Implemented data validation checks for integrity before loading.
- **Data Loading Performance**:
  - **Problem**: Slow loading of large CSV files.
  - **Solution**: Optimized loading using pandas and caching mechanisms in Streamlit.
- **Streamlit Update Compatibility**:
  - **Problem**: Compatibility issues with Streamlit updates.
  - **Solution**: Regularly updated codebase and tested for compatibility.
- **Foraging Data Integration**:
  - **Problem**: Difficulty in integrating foraging data.
  - **Solution**: Created a dedicated script and standardized data format for consistent processing and visualization.
## Conclusion
This app provides a comprehensive and interactive way to visualize the profitability of Stardew Valley items. It addresses the challenge of manually searching through the wiki and offers a flexible, data-driven solution that can be easily updated.


