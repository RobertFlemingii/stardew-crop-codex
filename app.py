import streamlit as st
from animal_products import animal_products_tab
from crops import crops_tab
from artisan_goods import artisan_goods_tab
from metal_bars import metal_bars_tab
from gems import gems_tab
from syrups import syrups_tab
from fishing import fishing_tab

# Set the page layout to wide and set page title
st.set_page_config(layout="wide", page_title="Stardew Valley Helper")

# Create sidebar for navigation
st.sidebar.title("Navigation")
selected_tab = st.sidebar.selectbox("Select Tab", ["Animal Products", "Crops", "Artisan Goods", "Metal Bars", "Gems", "Syrups", "Fishing"])

# Display the selected tab
if selected_tab == "Animal Products":
    animal_products_tab()
elif selected_tab == "Crops":
    crops_tab()
elif selected_tab == "Artisan Goods":
    artisan_goods_tab()
elif selected_tab == "Metal Bars":
    metal_bars_tab()
elif selected_tab == "Gems":
    gems_tab()
elif selected_tab == "Syrups":
    syrups_tab()
elif selected_tab == "Fishing":
    fishing_tab()
