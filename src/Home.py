import streamlit as st
import json

st.set_page_config(
    page_title="Home",
    page_icon="👋",
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
selected_customer = "John Doe"

st.session_state["selected_customer"] = "John Doe"
st.session_state["customer_selected"] = True
        




# Check if a customer has been selected
# if (st.session_state.get("portfolio_page") == "AI Generate Portfolio" and st.session_state.get("customer_selected", False)):
#     pages = ["Select Customer", "Customer Details", "AI Generate Portfolio"]
# if st.session_state.get("customer_selected", False):
#     pages = ["Select Customer", "Customer Details"]
# else:
#     pages = ["Select Customer"]



st.write("# Welcome to Rizq! 👋")


st.markdown(
    """
    How to use Rizq:
    1. Use AI generate for our interactive portfolio generator
"""
)