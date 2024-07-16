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
def calculate_modified_price(base_price, quality, selected_profession, profession, product):
    quality_multipliers = {'Default': 1, 'Silver': 1.25, 'Gold': 1.5, 'Iridium': 2}
    
    if quality not in quality_multipliers:
        raise ValueError(f"Invalid quality modifier: {quality}")

    quality_multiplier = quality_multipliers[quality]

    if selected_profession == 'Default':
        profession_multiplier = 1
    elif selected_profession == 'Rancher' and profession == 'Rancher':
        profession_multiplier = 1.2
    elif selected_profession == 'Artisan' and profession == 'Artisan':
        profession_multiplier = 1.4
    else:
        profession_multiplier = 1

    modified_price = base_price * quality_multiplier * profession_multiplier
    return math.floor(modified_price)


# Main function for the Streamlit app
def animal_products_tab():

    # Load the data
    df = load_data('animal_products_data.csv')

    # Ensure 'profession' column exists in the DataFrame
    if 'profession' not in df.columns:
        st.error("The 'profession' column is missing from the dataset.")
        return

    # Create columns for the select boxes to make the layout responsive
    col1, col2 = st.columns([1, 3])

    with col1:
        # Alphabetize Select Animal Product dropdown
        selected_product = st.selectbox('Select Animal Product', ['All/Any'] + sorted(list(df['product'].unique())))

        # Dropdown menus for selecting quality and profession modifiers
        selected_quality = st.selectbox('Select Quality Modifier', ['Default', 'Silver', 'Gold', 'Iridium'])
        selected_profession = st.selectbox('Select Profession Modifier', ['Default', 'Rancher', 'Artisan'])

    # Filter data based on selections
    filtered_df = df.copy()

    if selected_product != 'All/Any':
        filtered_df = filtered_df[filtered_df['product'] == selected_product]

    # Apply the modifiers to the prices
    filtered_df['price'] = filtered_df.apply(lambda row: calculate_modified_price(row['base_price'], selected_quality, selected_profession, row['profession'], row['product']), axis=1)

    # Aggregating data for bar chart
    agg_data = filtered_df.groupby('product').agg({
        'price': 'mean'  # Average price
    }).reset_index()

    # Check if there's data to show
    if selected_product != 'All/Any':
        st.write(f"## Details for {selected_product}")

        # Filter the DataFrame to get the details of the selected product
        product_details = df[df['product'] == selected_product].iloc[0]

        # Create a dictionary to hold the details
        product_info = {
            "Base Price (g)": product_details['base_price'],
            "Quality": selected_quality,
            "Selected Profession": selected_profession,
            "Actual Profession": product_details['profession'],
            "Modified Price": calculate_modified_price(product_details['base_price'], selected_quality, selected_profession, product_details['profession'], selected_product)
        }

        # Convert the dictionary to a DataFrame for display
        product_info_df = pd.DataFrame.from_dict(product_info, orient='index', columns=['Details'])

        # Display the table
        with col2:
            st.table(product_info_df)

    elif agg_data.empty:
        st.write("### No data to display with current filters.")
    else:
        # Bar chart for average prices using plotly
        with col2:
            st.write("## Bar Chart of Average Prices")
            fig = px.bar(
                agg_data,
                x='product',
                y='price',
                text=None,
                hover_data={'price': True},
                title='Average Animal Product Prices'
            )

            # Customize the bars
            fig.update_traces(
                texttemplate='',
                hovertemplate='<b>%{x}</b><br>Price: %{y:.0f}g<extra></extra>',
            )

            # Rotate x-axis labels
            fig.update_layout(
                xaxis_title='Animal Product',
                yaxis_title='Price (g)',
                title='Average Animal Product Prices',
                xaxis={'tickangle': -90}
            )

            st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    animal_products_tab()
