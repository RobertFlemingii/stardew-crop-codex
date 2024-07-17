import pandas as pd
import streamlit as st
import plotly.express as px

# Function to load data with caching
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Calculate modified prices
def calculate_modified_prices(df, profession):
    if profession == "Gemologist":
        df.loc[df["profession"] == "Gemologist", "price"] *= 1.3
    elif profession == "Blacksmith":
        df.loc[df["profession"] == "Blacksmith", "price"] *= 1.5
    return df

def mining_tab():
    st.title("Mining")

    df = load_data('mine_data.csv')

    col1, col2 = st.columns([1, 3])

    with col1:
        selected_mineral = st.selectbox("Select Mineral", ["Any"] + df["name"].unique().tolist())
        locations = st.multiselect(
            "Select Location(s)",
            ["", "1-39", "41-79", "81-120", "Skull Cavern", "Quarry", "Quarry Mine", "Hill-top Farm", "Volcano Dungeon", "Ginger Island"],
            default=[]
        )
        exclusive_locations = st.checkbox("Exclusive Location Selection")

        exclude_geode_minerals = st.checkbox("Exclude Geode Minerals", value=True)

        profession = st.selectbox("Select Profession", ["Any", "Gemologist", "Blacksmith"])

    if profession != "Any":
        df = calculate_modified_prices(df, profession)

    if exclusive_locations:
        if locations:
            df = df[df[locations].all(axis=1)]
        else:
            df = pd.DataFrame(columns=df.columns)  # Empty DataFrame if no locations selected
    elif locations:
        df = df[df[locations].any(axis=1)]

    if exclude_geode_minerals:
        df = df[df["type"] != "geode minerals"]

    with col2:
        if selected_mineral != "Any":
            selected_mineral_df = df[df["name"] == selected_mineral]
            st.write(selected_mineral_df[["name", "price", "type", "profession"]])
        else:
            fig = px.bar(
                df,
                x="name",
                y="price",
                hover_data=["type", "profession"],
                title="Prices of Minerals",
                labels={"name": "Mineral Name", "price": "Price"}
            )
            fig.update_layout(
                xaxis={'categoryorder':'total ascending', 'tickangle': -90},
                yaxis_type="log"
            )
            st.plotly_chart(fig)

# Testing the function
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Mining Tab Test")
    mining_tab()
