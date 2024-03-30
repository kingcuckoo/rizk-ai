import streamlit as st
import json
from manual_build_portfolio import manual_build_portfolio_page
from ai_generate_portfolio import ai_generate_portfolio_page

def read_customer_info():
    # Path to your JSON file
    file_path = './storage.json'
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Read Customer info
customer_JSON = read_customer_info()

# Define the layout for the first page
def page1():
    st.title("Select a Customer")

    # List of customers
    customers = [customer["Customer"]["Name"] for customer in st.session_state.get("CUSTOMER_JSON")["Financial Advisor"]]

    # Dropdown for selecting a customer
    selected_customer = st.selectbox("Choose a customer", options=customers)

    # Button to confirm selection
    if st.button("Confirm Selection"):
        if selected_customer:
            st.success(f"You have selected {selected_customer}")
            # Store the selected customer in session state
            st.session_state["selected_customer"] = selected_customer
            st.session_state["customer_selected"] = True
            st.experimental_rerun()
        else:
            st.error("Please select a customer")


# Define the layout for the second page
def page2():
    st.title("Customer Details")
    # Retrieve the selected customer from session state
    selected_customer = st.session_state.get("selected_customer", "No customer selected")
    
    # Find the selected customer's data in the JSON
    customer_data = next((customer for customer in st.session_state.get("CUSTOMER_JSON")["Financial Advisor"] if customer["Customer"]["Name"] == selected_customer), None)
    
    if customer_data:
        st.write(f"Details for {selected_customer}:")
        
        # Iterate through the portfolios of the selected customer
        for portfolio in customer_data["Customer"]["Portfolio"]:            
                # Create an accordion (expander) for each portfolio
                with st.expander(portfolio["Portfolio Name"]):
                    st.write("Stocks bought:")
                    for stock in portfolio["Portfolio item"]["Stocks bought"]:
                        st.write(f"- {stock['Name']} (Ticker: {stock['Ticker']}, Purchase Price: {stock['Purchase price']}, Quantity: {stock['Quantity']})")
                    st.write(f"Last calculated risk scores: {portfolio['Portfolio item']['Last calculated risk scores']}")
                    st.write(f"Max money to invest in this Portfolio: {portfolio['Portfolio item']['Max money to invest in this Portfolio']}")
                    st.write(f"Preferred risk for Portfolio: {portfolio['Portfolio item']['Preferred risk for Portfolio']}")
    else:
        st.write("Customer not found or no portfolios available.")

    # Create a row with two columns for the buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("AI Generate Portfolio"):
            st.session_state["portfolio_page"] = "AI Generate Portfolio"
            st.experimental_rerun()
    with col2:
        if st.button("Manual Build Portfolio"):
            st.session_state["portfolio_page"] = "Manual Build Portfolio"
            st.experimental_rerun()


# Main app logic
def main():
    st.sidebar.title("Navigation")
    # Check if a customer has been selected
    if (st.session_state.get("portfolio_page") == "Manual Build Portfolio" or st.session_state.get("portfolio_page") == "AI Generate Portfolio"):
        if st.session_state.get("portfolio_page") == "Manual Build Portfolio" : 
            pages = ["Select Customer", "Customer Details", "Manual Build Portfolio"]            
        if st.session_state.get("portfolio_page") == "AI Generate Portfolio":
            pages = ["Select Customer", "Customer Details", "AI Generate Portfolio"]
    elif st.session_state.get("customer_selected", False):
        pages = ["Select Customer", "Customer Details"]
    else:
        pages = ["Select Customer"]

    st.session_state["CUSTOMER_JSON"] = customer_JSON

    page = st.sidebar.radio("Go to", pages)

    if page == "Select Customer":
        page1()
    elif page == "Customer Details":
        page2()
    elif page == "AI Generate Portfolio":
        ai_generate_portfolio_page()
    elif page == "Manual Build Portfolio":
        manual_build_portfolio_page()


if __name__ == "__main__":
    main()
