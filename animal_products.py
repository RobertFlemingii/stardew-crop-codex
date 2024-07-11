import streamlit as st
import pandas as pd

def animal_products_tab():
    st.title("Animal Products Data")

    # Sample farming data
    data = {
        "Crops": ["Wheat", "Corn", "Potato"],
        "Seasons": ["Spring", "Summer", "Fall"],
        "Prices": [50, 75, 100]
    }
    
    df = pd.DataFrame(data)
    
    # Display the data in a table
    # st.table(df)
