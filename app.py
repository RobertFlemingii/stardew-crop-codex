import streamlit as st
from tilling import tilling_tab  # Import your tab functions
from ranching import ranching_tab
from mining import mining_tab
from foraging import foraging_tab
from fishing import fishing_tab

# Define the main menu function
def main_menu():
    st.title("Stardew Valley Data Visualization")
    st.write("## Main Menu")
    st.write("Click on the icons below to navigate to different sections:")

    # Create big icons for each section in the desired order
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("Tilling", key='tilling'):
            st.session_state.page = 'Tilling'

    with col2:
        if st.button("Ranching", key='ranching'):
            st.session_state.page = 'Ranching'

    with col3:
        if st.button("Mining", key='mining'):
            st.session_state.page = 'Mining'

    with col4:
        if st.button("Foraging", key='foraging'):
            st.session_state.page = 'Foraging'

    with col5:
        if st.button("Fishing", key='fishing'):
            st.session_state.page = 'Fishing'

# Main function to run the Streamlit app
def main():
    # Initialize session state to manage page navigation
    session_state = st.session_state
    if 'page' not in session_state:
        session_state.page = 'Main Menu'

    # Display the sidebar navigation and main content
    st.sidebar.title("Navigation")
    nav_selection = st.sidebar.radio("Go to", ["Main Menu", "Tilling", "Ranching", "Mining", "Foraging", "Fishing"])

    if nav_selection == "Main Menu":
        main_menu()
    elif nav_selection == "Tilling":
        tilling_tab()  # Replace with your tilling tab function
    elif nav_selection == "Ranching":
        ranching_tab()  # Replace with your ranching tab function
    elif nav_selection == "Mining":
        mining_tab()  # Replace with your mining tab function
    elif nav_selection == "Foraging":
        foraging_tab()  # Replace with your foraging tab function
    elif nav_selection == "Fishing":
        fishing_tab()  # Replace with your fishing tab function

# Run the Streamlit app
if __name__ == '__main__':
    main()
