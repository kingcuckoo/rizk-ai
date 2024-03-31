import streamlit as st
import json

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
    customers = [customer["Customer"]["Name"] for customer in customer_JSON["Financial Advisor"]]

    # Dropdown for selecting a customer
    selected_customer = st.selectbox("Choose a customer", options=customers)

    # Button to confirm selection
    if st.button("Confirm Selection"):
        if selected_customer:
            st.success(f"You have selected {selected_customer}")
            # Store the selected customer in session state
            st.session_state["selected_customer"] = selected_customer
            st.session_state["customer_selected"] = True
            st.elsxperimental_rerun()
        else:
            st.error("Please select a customer")


# Define the layout for the second page
def page2():
    st.title("Customer Details")
    # Retrieve the selected customer from session state
    selected_customer = st.session_state.get("selected_customer", "No customer selected")
    
    # Find the selected customer's data in the JSON
    customer_data = next((customer for customer in customer_JSON["Financial Advisor"] if customer["Customer"]["Name"] == selected_customer), None)
    
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


# Main app logic
def main():
    st.sidebar.title("Navigation")
    pages = ["Select Customer", "Customer Details"]

    st.session_state["CUSTOMER_JSON"] = customer_JSON

    # Check if a customer has been selected
    if st.session_state.get("customer_selected", False):
        page = st.sidebar.radio("Go to", pages)
    else:
        page = st.sidebar.radio("Go to", [pages[0]])

    if page == "Select Customer":
        page1()
    elif page == "Customer Details":
        page2()

if __name__ == "__main__":
    main()
