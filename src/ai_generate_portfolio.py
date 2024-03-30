import streamlit as st

# Define the layout for the AI Generate Portfolio page
def ai_generate_portfolio_page():
    # Retrieve the selected customer from session state
    selected_customer = st.session_state.get("selected_customer", "No customer selected")

    st.title("AI Generate Portfolio")
    st.write("This page will show the AI generated portfolio.")


    st.write(f"Details for {selected_customer}:")