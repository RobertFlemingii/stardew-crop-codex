import streamlit as st
import pandas as pd
import plotly.express as px
import math

# Function to load data with caching
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to calculate modified price based on quality and profession
def calculate_modified_price(price, quality, selected_profession, profession, forage):
    quality_multipliers = {'Default': 1, 'Silver': 1.25, 'Gold': 1.5, 'Iridium': 2}

    if quality not in quality_multipliers:
        raise ValueError(f"Invalid quality modifier: {quality}")

    quality_multiplier = quality_multipliers[quality]

    if selected_profession == 'Default':
        profession_multiplier = 1
    elif selected_profession == 'Artisan' and profession == 'Artisan':
        profession_multiplier = 1.4
    else:
        profession_multiplier = 1

    modified_price = price * quality_multiplier * profession_multiplier
    return math.floor(modified_price)

# Main function for the Foraging tab
def foraging_tab():

    # Load the data
    df = load_data('foraging_data.csv')  # Adjust file path as per your data file

    # Ensure required columns are present
    required_columns = ['forage', 'price', 'profession', 'spring', 'summer', 'fall', 'winter',
                        'backwoods', 'beach', 'bus stop', 'bushes', 'cindersnap forest',
                        'desert', 'farm cave', 'forest farm', 'ginger island', 'mines',
                        'mountain', 'pelican town', 'railroad', 'secret woods', 'soil', 'trees']

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        st.error(f"The following columns are missing in the dataset: {', '.join(missing_columns)}")
        return

    # Create columns for the select boxes to make the layout responsive
    col1, col2 = st.columns([1, 3])

    with col1:
        # Alphabetize Select forage dropdown
        selected_forage = st.selectbox('Select Forageable', ['All/Any'] + sorted(list(df['forage'].unique())))

        # Dropdown menus for selecting quality and profession modifiers
        selected_quality = st.selectbox('Select Quality Modifier', ['Default', 'Silver', 'Gold', 'Iridium'])
        selected_profession = st.selectbox('Select Profession Modifier', ['Default', 'Artisan'])

        # Season selection with default state
        selected_season = st.selectbox('Select Season', ['All Seasons', 'Spring', 'Summer', 'Fall', 'Winter'], index=0)

        # Exclusive season selection
        exclusive_season = st.checkbox('Exclusive Season')

        # Location selection with default state
        selected_location = st.selectbox('Select Location', ['All Locations', 'Backwoods', 'Beach', 'Bus Stop', 'Bushes', 'Cindersnap Forest',
                                                             'Desert', 'Farm Cave', 'Forest Farm', 'Ginger Island',
                                                             'Mines', 'Mountain', 'Pelican Town', 'Railroad',
                                                             'Secret Woods', 'Soil', 'Trees'], index=0)

        # Exclusive location selection
        exclusive_location = st.checkbox('Exclusive Location')

    # Filter data based on selections
    filtered_df = df.copy()

    if selected_forage != 'All/Any':
        filtered_df = filtered_df[filtered_df['forage'] == selected_forage]

    if selected_season != 'All Seasons':
        if exclusive_season:
            filtered_df = filtered_df[filtered_df[selected_season.lower()] == 1]
        else:
            filtered_df = filtered_df[filtered_df[selected_season.lower()] >= 1]

    if selected_location != 'All Locations':
        if exclusive_location:
            filtered_df = filtered_df[filtered_df[selected_location.lower()] == 1]
        else:
            filtered_df = filtered_df[filtered_df[selected_location.lower()] >= 1]

    # Apply the modifiers to the prices
    filtered_df['price'] = filtered_df.apply(lambda row: calculate_modified_price(row['price'], selected_quality, selected_profession, row['profession'], row['forage']), axis=1)

    # Aggregating data for bar chart
    agg_data = filtered_df.groupby('forage').agg({
        'price': 'mean'  # Average price
    }).reset_index()

    # Check if there's data to show
    if selected_forage != 'All/Any':
        st.write(f"## Details for {selected_forage}")

        # Filter the DataFrame to get the details of the selected forage
        forage_details = df[df['forage'] == selected_forage].iloc[0]

        # Create a dictionary to hold the details
        forage_info = {
            "Base Price (g)": forage_details['price'],
            "Quality": selected_quality,
            "Selected Profession": selected_profession,
            "Actual Profession": forage_details['profession'],
            "Modified Price": calculate_modified_price(forage_details['price'], selected_quality, selected_profession, forage_details['profession'], selected_forage)
        }

        # Convert the dictionary to a DataFrame for display
        forage_info_df = pd.DataFrame.from_dict(forage_info, orient='index', columns=['Details'])

        # Display the table
        with col2:
            st.table(forage_info_df)

    elif agg_data.empty:
        st.write("### No data to display with current filters.")
    else:
        # Sort data by increasing price
        agg_data = agg_data.sort_values(by='price')

        # Bar chart for average prices using plotly
        with col2:
            st.write("## Bar Chart of Average Prices")
            fig = px.bar(
                agg_data,
                x='forage',
                y='price',
                text=None,
                hover_data={'price': True},
                title='Average Forageable Prices'
            )

            # Customize the bars
            fig.update_traces(
                texttemplate='',
                hovertemplate='<b>%{x}</b><br>Price: %{y:.0f}g<extra></extra>',
            )

            # Rotate x-axis labels
            fig.update_layout(
                xaxis_title='Forageable',
                yaxis_title='Price (g)',
                title='Average Forageable Prices',
                xaxis={'tickangle': -90},
                yaxis_type='log'  # Set y-axis to logarithmic scale
            )

            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    foraging_tab()
