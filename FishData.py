import streamlit as st
import pandas as pd

# Template for printing text and plotting line chart ##########################

# st.write("""
# # My first app
# Look at the little *fishies!*
# """)

# df = pd.read_csv("fish_data.csv")
# st.bar_chart(df)

# Template for printing text and making a slider ##############################

# st.write("""
# # Apps with widgets!
# """)

# x = st.slider("Select a number")
# st.write("You selected", x)

# Implementation ##############################################################

import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv('fish_data.csv')

# Display the raw data
st.title("Fish Data Visualization")
st.write("## Raw Data")
st.write(df)

# Display column names for debugging
st.write("## Column Names")
st.write(df.columns)

# Dropdown menu for selecting fish
selected_fish = st.selectbox('Select Fish', ['All/Any'] + list(df['name'].unique()))

# Dropdown menus for other filters
locations = ['All/Any', 'ocean', 'river', 'pond', 'lake', 'waterfall', 'woods', 'sewer', 'swamp', 'mines', 'desert', 'bug lair', 'cove', 'ginger ocean', 'ginger pond', 'ginger river', 'volcano']
times_of_day = ['All/Any', 'morning', 'afternoon', 'evening', 'night']
seasons = ['All/Any', 'spring', 'summer', 'fall', 'winter']
weather_conditions = ['All/Any', 'sun', 'rain', 'wind']

selected_location = st.selectbox('Select Location', locations)
selected_time = st.selectbox('Select Time of Day', times_of_day)
selected_season = st.selectbox('Select Season', seasons)
selected_weather = st.selectbox('Select Weather', weather_conditions)

# Filter data based on selections
filtered_df = df.copy()

if selected_fish != 'All/Any':
    filtered_df = filtered_df[filtered_df['name'] == selected_fish]

if selected_location != 'All/Any':
    filtered_df = filtered_df[filtered_df[selected_location] == 1]

if selected_time != 'All/Any':
    filtered_df = filtered_df[filtered_df[selected_time] == 1]

if selected_season != 'All/Any':
    filtered_df = filtered_df[filtered_df[selected_season] == 1]

if selected_weather != 'All/Any':
    filtered_df = filtered_df[filtered_df[selected_weather] == 1]

# Aggregating data for bar chart
agg_data = filtered_df.groupby('name').agg({
    'price': 'mean',  # Average price
    'ocean': 'sum', 'river': 'sum', 'pond': 'sum', 'lake': 'sum', 'waterfall': 'sum', 
    'woods': 'sum', 'sewer': 'sum', 'swamp': 'sum', 'mines': 'sum', 'desert': 'sum', 
    'bug lair': 'sum', 'cove': 'sum', 'ginger ocean': 'sum', 'ginger pond': 'sum', 
    'ginger river': 'sum', 'volcano': 'sum', 'morning': 'sum', 'afternoon': 'sum', 
    'evening': 'sum', 'night': 'sum', 'spring': 'sum', 'summer': 'sum', 'fall': 'sum', 
    'winter': 'sum', 'sun': 'sum', 'rain': 'sum', 'wind': 'sum'
}).reset_index()

st.write("## Filtered and Aggregated Data")
st.write(agg_data)

# Bar chart for average prices
st.write("## Bar Chart of Average Prices")
st.bar_chart(agg_data[['name', 'price']].set_index('name'))

# Additional charts for other comparisons
st.write("## Other Comparisons")

# Locations
if selected_location != 'All/Any':
    st.write(f"### Presence in {selected_location.capitalize()}")
    st.bar_chart(agg_data[['name', selected_location]].set_index('name'))

# Times of Day
if selected_time != 'All/Any':
    st.write(f"### Presence during {selected_time.capitalize()}")
    st.bar_chart(agg_data[['name', selected_time]].set_index('name'))

# Seasons
if selected_season != 'All/Any':
    st.write(f"### Presence in {selected_season.capitalize()}")
    st.bar_chart(agg_data[['name', selected_season]].set_index('name'))

# Weather Conditions
if selected_weather != 'All/Any':
    st.write(f"### Presence in {selected_weather.capitalize()} Weather")
    st.bar_chart(agg_data[['name', selected_weather]].set_index('name'))

