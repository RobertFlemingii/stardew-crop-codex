import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv('fish_data.csv')

# Display the raw data
st.title("Fish Data Visualization")
st.write("## Raw Data")
st.write(df)

# # Display column names for debugging
# st.write("## Column Names")
# st.write(df.columns)

# Dropdown menu for selecting fish
selected_fish = st.selectbox('Select Fish', ['All/Any'] + list(df['name'].unique()))

# Multiselect menus for other filters
locations = ['ocean', 'river', 'pond', 'lake', 'waterfall', 'woods', 'sewer', 'swamp', 'mines', 'desert', 'bug lair', 'cove', 'ginger ocean', 'ginger pond', 'ginger river', 'volcano']
times_of_day = ['morning', 'afternoon', 'evening', 'night']
seasons = ['spring', 'summer', 'fall', 'winter']
weather_conditions = ['sun', 'rain', 'wind']

# Function to create dynamic multiselect with "All/Any" handling
def dynamic_multiselect(label, options, default='All/Any'):
    selected = st.multiselect(label, [default] + options, default=default)
    if len(selected) == 0 or (default in selected and len(selected) > 1):
        selected.remove(default)
    elif default in selected:
        selected = options
    return selected

selected_locations = dynamic_multiselect('Select Locations', locations)
exclusive_locations = st.checkbox('Exclusive Locations')
selected_times = dynamic_multiselect('Select Times of Day', times_of_day)
exclusive_times = st.checkbox('Exclusive Times of Day')
selected_seasons = dynamic_multiselect('Select Seasons', seasons)
exclusive_seasons = st.checkbox('Exclusive Seasons')
selected_weather = dynamic_multiselect('Select Weather', weather_conditions)
exclusive_weather = st.checkbox('Exclusive Weather')

# Filter data based on selections
filtered_df = df.copy()

if selected_fish != 'All/Any':
    filtered_df = filtered_df[filtered_df['name'] == selected_fish]

def apply_exclusivity_filter(filtered_df, selected_options, exclusivity, columns):
    if 'All/Any' not in selected_options:
        if exclusivity:
            filter_mask = filtered_df[columns].apply(lambda row: all(row[selected_options]) and not any(row[[col for col in columns if col not in selected_options]]), axis=1)
        else:
            filter_mask = filtered_df[columns].apply(lambda row: any(row[selected_options]), axis=1)
        filtered_df = filtered_df[filter_mask]
    return filtered_df

filtered_df = apply_exclusivity_filter(filtered_df, selected_locations, exclusive_locations, locations)
filtered_df = apply_exclusivity_filter(filtered_df, selected_times, exclusive_times, times_of_day)
filtered_df = apply_exclusivity_filter(filtered_df, selected_seasons, exclusive_seasons, seasons)
filtered_df = apply_exclusivity_filter(filtered_df, selected_weather, exclusive_weather, weather_conditions)

# Aggregating data for bar chart
agg_data = filtered_df.groupby('name').agg({
    'price': 'mean',  # Average price
    **{col: 'sum' for col in locations + times_of_day + seasons + weather_conditions}
}).reset_index()

# Check if there's data to show
if agg_data.empty:
    st.write("### No data to display with current filters.")
else:
    st.write("## Filtered and Aggregated Data")
    st.write(agg_data)

    # Bar chart for average prices
    st.write("## Bar Chart of Average Prices")
    if len(agg_data) > 10:
        # Adjust figure size for better readability
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.bar_chart(agg_data[['name', 'price']].set_index('name'), use_container_width=False)
    else:
        st.bar_chart(agg_data[['name', 'price']].set_index('name'))
        

    # # Additional charts for other comparisons
    # if selected_locations and 'All/Any' not in selected_locations:
    #     for loc in selected_locations:
    #         st.write(f"### Presence in {loc.capitalize()}")
    #         st.bar_chart(agg_data[['name', loc]].set_index('name'))

    # if selected_times and 'All/Any' not in selected_times:
    #     for time in selected_times:
    #         st.write(f"### Presence during {time.capitalize()}")
    #         st.bar_chart(agg_data[['name', time]].set_index('name'))

    # if selected_seasons and 'All/Any' not in selected_seasons:
    #     for season in selected_seasons:
    #         st.write(f"### Presence in {season.capitalize()}")
    #         st.bar_chart(agg_data[['name', season]].set_index('name'))

    # if selected_weather and 'All/Any' not in selected_weather:
    #     for weather in selected_weather:
    #         st.write(f"### Presence in {weather.capitalize()} Weather")
    #         st.bar_chart(agg_data[['name', weather]].set_index('name'))
