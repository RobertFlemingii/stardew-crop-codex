import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, calculate_modified_price

def fishing_tab():
    st.title("Fishing Data")
    
    # Load the data
    df = load_data('fish_data.csv')

    # Create columns for the select boxes to make the layout responsive
    col1, col2 = st.columns([1, 3])

    with col1:
        # Alphabetize Select Fish dropdown
        selected_fish = st.selectbox('Select Fish', ['All/Any'] + sorted(list(df['name'].unique())))

        # Multiselect menus for other filters
        locations = ['ocean', 'river', 'pond', 'lake', 'waterfall', 'woods', 'sewer', 'swamp', 'mines', 'desert', 'mutant bug lair', 'cove', 'ginger ocean', 'ginger pond', 'ginger river', 'volcano', 'night market']
        times_of_day = ['morning', 'afternoon', 'evening', 'night']
        seasons = ['spring', 'summer', 'fall', 'winter']
        weather_conditions = ['sun', 'rain', 'wind']

        # Function to create dynamic multiselect without "All/Any" handling
        def dynamic_multiselect(label, options):
            selected = st.multiselect(label, options)
            if len(selected) == 0:
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

        # Checkboxes for excluding fish categories (checked by default)
        exclude_night_market = st.checkbox('Exclude Night Market Fish', value=True)
        exclude_legendary_1 = st.checkbox('Exclude Legendary Fish I', value=True)
        exclude_legendary_2 = st.checkbox('Exclude Legendary Fish II', value=True)

        # Dropdown menus for selecting quality and profession modifiers
        selected_quality = st.selectbox('Select Quality Modifier', ['Default', 'Silver', 'Gold', 'Iridium'])
        selected_profession = st.selectbox('Select Profession Modifier', ['Default', 'Fisher', 'Angler'])

    # Filter data based on selections
    filtered_df = df.copy()

    if selected_fish != 'All/Any':
        filtered_df = filtered_df[filtered_df['name'] == selected_fish]

    def apply_exclusivity_filter(filtered_df, selected_options, exclusivity, columns):
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

    # Exclude fish types based on checkboxes
    if exclude_night_market:
        filtered_df = filtered_df[filtered_df['type'] != 'night market']
    if exclude_legendary_1:
        filtered_df = filtered_df[filtered_df['type'] != 'legendary']
    if exclude_legendary_2:
        filtered_df = filtered_df[filtered_df['type'] != 'legendary II']

    # Apply the modifiers to the prices
    filtered_df['price'] = filtered_df['price'].apply(lambda x: calculate_modified_price(x, selected_quality, selected_profession))

    # Aggregating data for bar chart
    agg_data = filtered_df.groupby('name').agg({
        'price': 'mean',  # Average price
        **{col: 'sum' for col in locations + times_of_day + seasons + weather_conditions}
    }).reset_index()

    # Check if there's data to show
    if selected_fish != 'All/Any':
        st.write(f"## Details for {selected_fish}")

        # Filter the DataFrame to get the details of the selected fish
        fish_details = df[df['name'] == selected_fish].iloc[0]

        # Create a dictionary to hold the details
        fish_info = {
            "Price (g)": fish_details['price'],
            "Locations": ", ".join([loc for loc in locations if fish_details[loc] == 1]),
            "Times of Day": ", ".join([time for time in times_of_day if fish_details[time] == 1]),
            "Seasons": ", ".join([season for season in seasons if fish_details[season] == 1]),
            "Weather Conditions": ", ".join([weather for weather in weather_conditions if fish_details[weather] == 1])
        }

        # Convert the dictionary to a DataFrame for display
        fish_info_df = pd.DataFrame.from_dict(fish_info, orient='index', columns=['Details'])

        # Display the table
        with col2:
            st.table(fish_info_df)

    elif agg_data.empty:
        st.write("### No data to display with current filters.")
    else:
        # Bar chart for average prices using plotly
        with col2:
            st.write("## Bar Chart of Average Prices")
            fig = px.bar(
                agg_data,
                x='name',
                y='price',
                text=None,
                hover_data={'price': True},
                title='Average Fish Prices'
            )

            # Customize the bars
            fig.update_traces(
                texttemplate='',
                hovertemplate='<b>%{x}</b><br>Price: %{y:.0f}g<extra></extra>',
            )

            # Rotate x-axis labels
            fig.update_layout(
                xaxis_title='Fish Name',
                yaxis_title='Price (g)',
                title='Average Fish Prices',
                xaxis={'tickangle': -90}
            )

            st.plotly_chart(fig, use_container_width=True)
