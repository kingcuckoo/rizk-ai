import streamlit as st
import json

st.set_page_config(
    page_title="Select Customer"
)


def read_customer_info():
    # Path to your JSON file
    file_path = './storage.json'
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Read Customer info
customer_JSON = read_customer_info()
st.session_state["CUSTOMER_JSON"] = customer_JSON

#TODO: Saiket add homepage info

# List of customers
customers = [customer["Customer"]["Name"] for customer in st.session_state.get("CUSTOMER_JSON")]

# Dropdown for selecting a customer
selected_customer = st.selectbox("Choose a customer", options=customers)

# Button to confirm selection
if st.button("Confirm Selection"):
    if selected_customer:
        st.success(f"You have selected {selected_customer}")
        print(f"You have selected {selected_customer}")
        # Store the selected customer in session state
        st.session_state["selected_customer"] = selected_customer
        st.session_state["customer_selected"] = True
        st.experimental_rerun()
    else:
        st.error("Please select a customer")




# Check if a customer has been selected
# if (st.session_state.get("portfolio_page") == "AI Generate Portfolio" and st.session_state.get("customer_selected", False)):
#     pages = ["Select Customer", "Customer Details", "AI Generate Portfolio"]
# if st.session_state.get("customer_selected", False):
#     pages = ["Select Customer", "Customer Details"]
# else:
#     pages = ["Select Customer"]

