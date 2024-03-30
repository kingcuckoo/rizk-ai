import streamlit as st


# Define the layout for the Manual Build Portfolio page
def manual_build_portfolio_page():

    # Retrieve the selected customer from session state
    selected_customer = st.session_state.get("selected_customer", "No customer selected")


    st.title("Manual Build Portfolio")
    st.write("This page will allow you to manually build a portfolio.")

    st.write(f"Details for {selected_customer}:")