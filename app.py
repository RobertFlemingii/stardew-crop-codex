import streamlit as st
from tilling import tilling_tab  
from ranching import ranching_tab
from mining import mining_tab
from foraging import foraging_tab
from fishing import fishing_tab

# Set the page configuration
st.set_page_config(
    page_title="Stardew Valley Data Visualization",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to handle page navigation
def navigate_to(page):
    st.session_state.page = page
    st.session_state.nav_selection = page
    st.rerun()

# Define the main menu function
def main_menu():
    st.title("Stardew Valley Data Visualization")
    st.write("## Main Menu")
    st.write("Click on the icons below to navigate to different sections:")

    # Load icons 
    tilling_icon = 'icons/Tilling.png'
    ranching_icon = 'icons/Ranching.png'
    mining_icon = 'icons/Mining.png'
    foraging_icon = 'icons/Foraging.png'
    fishing_icon = 'icons/Fishing.png'

    # Create columns for the icons
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("Tilling", key='tilling'):
            navigate_to('Tilling')
        st.image(tilling_icon, use_column_width=True)

    with col2:
        if st.button("Ranching", key='ranching'):
            navigate_to('Ranching')
        st.image(ranching_icon, use_column_width=True)

    with col3:
        if st.button("Mining", key='mining'):
            navigate_to('Mining')
        st.image(mining_icon, use_column_width=True)

    with col4:
        if st.button("Foraging", key='foraging'):
            navigate_to('Foraging')
        st.image(foraging_icon, use_column_width=True)

    with col5:
        if st.button("Fishing", key='fishing'):
            navigate_to('Fishing')
        st.image(fishing_icon, use_column_width=True)

# Main function to run the Streamlit app
def main():
    # Initialize session state to manage page navigation
    if 'page' not in st.session_state:
        st.session_state.page = 'Main Menu'
    if 'nav_selection' not in st.session_state:
        st.session_state.nav_selection = 'Main Menu'

    # Display the side taskbar
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            width: 200px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.title("Navigation")
    nav_selection = st.sidebar.radio("Go to", ["Main Menu", "Tilling", "Ranching", "Mining", "Foraging", "Fishing"], index=["Main Menu", "Tilling", "Ranching", "Mining", "Foraging", "Fishing"].index(st.session_state.nav_selection))

    # Update the session state based on sidebar navigation
    if nav_selection != st.session_state.page:
        navigate_to(nav_selection)

    # Display the appropriate page based on the session state
    if st.session_state.page == "Main Menu":
        main_menu()
    elif st.session_state.page == "Tilling":
        tilling_tab()  
    elif st.session_state.page == "Ranching":
        ranching_tab()  
    elif st.session_state.page == "Mining":
        mining_tab()  
    elif st.session_state.page == "Foraging":
        foraging_tab()  
    elif st.session_state.page == "Fishing":
        fishing_tab()  

# Run the Streamlit app
if __name__ == '__main__':
    main()
