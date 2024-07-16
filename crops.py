import streamlit as st
import pandas as pd
import plotly.express as px

def crops_tab():
    st.title("Crop Data")
    
    # Load the data
    df = load_data('crops_data.csv')  # Assuming you have a function to load crop data
    
    # Create columns for the select boxes to make the layout responsive
    col1, col2 = st.columns([1, 3])

    with col1:
        # Alphabetize Select Crop dropdown
        selected_crop = st.selectbox('Select Crop', ['All/Any'] + sorted(list(df['Crop'].unique())))

        # Dropdown menus for selecting quality and profession modifiers
        selected_quality = st.selectbox('Select Quality Modifier', ['Default', 'Silver', 'Gold', 'Iridium'])
        selected_profession = st.selectbox('Select Profession Modifier', ['Default', 'Fisher', 'Angler'])

        # Multiselect menu for selecting seasons
        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        selected_seasons = st.multiselect('Select Seasons', seasons)

        # Checkbox for exclusive season selection
        exclusive_seasons = st.checkbox('Exclusive Seasons')

    # Filter data based on selections
    filtered_df = df.copy()

    if selected_crop != 'All/Any':
        filtered_df = filtered_df[filtered_df['Crop'] == selected_crop]

    # Apply the modifiers to the sell prices
    filtered_df['Sell Price'] = filtered_df.apply(lambda row: calculate_modified_price(row['Sell Price'], selected_quality, selected_profession), axis=1)

    # Function to apply exclusivity filter
    def apply_exclusivity_filter(filtered_df, selected_options, exclusivity, columns):
        if exclusivity:
            filter_mask = filtered_df[columns].apply(lambda row: all(row[selected_options]) and not any(row[[col for col in columns if col not in selected_options]]), axis=1)
        else:
            filter_mask = filtered_df[columns].apply(lambda row: any(row[selected_options]), axis=1)
        filtered_df = filtered_df[filter_mask]
        return filtered_df

    # Apply season filter
    if selected_seasons:
        filtered_df = apply_exclusivity_filter(filtered_df, selected_seasons, exclusive_seasons, seasons)

    # Aggregating data for bar chart
    agg_data = filtered_df.groupby('Crop').agg({
        'Sell Price': 'mean',  # Average sell price
        # Add other aggregations if needed
    }).reset_index()

    # Check if there's data to show
    if selected_crop != 'All/Any':
        st.write(f"## Details for {selected_crop}")

        # Filter the DataFrame to get the details of the selected crop
        crop_details = df[df['Crop'] == selected_crop].iloc[0]

        # Create a dictionary to hold the details
        crop_info = {
            "Sell Price": crop_details['Sell Price'],
            # Add other details as needed
        }

        # Convert the dictionary to a DataFrame for display
        crop_info_df = pd.DataFrame.from_dict(crop_info, orient='index', columns=['Details'])

        # Display the table
        with col2:
            st.table(crop_info_df)

    elif agg_data.empty:
        st.write("### No data to display with current filters.")
    else:
        # Bar chart for average sell prices using plotly
        with col2:
            st.write("## Bar Chart of Average Sell Prices")
            fig = px.bar(
                agg_data,
                x='Crop',
                y='Sell Price',
                text=None,
                hover_data={'Sell Price': True},
                title='Average Crop Sell Prices'
            )

            # Customize the bars
            fig.update_traces(
                texttemplate='',
                hovertemplate='<b>%{x}</b><br>Sell Price: %{y:.0f}<extra></extra>',
            )

            # Rotate x-axis labels
            fig.update_layout(
                xaxis_title='Crop Name',
                yaxis_title='Sell Price',
                title='Average Crop Sell Prices',
                xaxis={'tickangle': -90}
            )

            st.plotly_chart(fig, use_container_width=True)
