import streamlit as st
import pandas as pd

# Function to load CSS
def load_css(file_path):
    with open(file_path, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Function to load data with caching
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to calculate modified price based on quality and profession
def calculate_modified_price(base_price, quality, profession):
    import math
    quality_multipliers = {'Default': 1, 'Silver': 1.25, 'Gold': 1.5, 'Iridium': 2}
    profession_multipliers = {'Default': 1, 'Fisher': 1.25, 'Angler': 1.5}

    quality_multiplier = quality_multipliers[quality]
    profession_multiplier = profession_multipliers[profession]

    modified_price = base_price * quality_multiplier * profession_multiplier
    return math.floor(modified_price)
