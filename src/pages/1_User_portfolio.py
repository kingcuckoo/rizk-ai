import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portfolios")

st.title("Your Portfolios")
# Retrieve the selected customer from session state
selected_customer = st.session_state.get("selected_customer", "No customer selected")

# Find the selected customer's data in the JSON

customer_data = {
    "Customer": {
      "Name": "John Doe",
      "Portfolio": [
        {
          "Portfolio Name": "John Doe Priority",
          "Portfolio item": {
            "Stocks bought": [
              {
                "Name": "Apple Inc.",
                "Ticker": "AAPL",
                "Purchase price": 150.00,
                "Quantity": 10
              },
              {
                "Name": "Microsoft Corporation",
                "Ticker": "MSFT",
                "Purchase price": 250.00,
                "Quantity": 5
              }
            ],
            "Last calculated risk scores": 0.3,
            "Max money to invest in this Portfolio": 5000.00,
            "Preferred risk for Portfolio": 0.6
          }
        },
        {
          "Portfolio Name": "John Doe Secondary",
          "Portfolio item": {
            "Stocks bought": [
              {
                "Name": "Pear Inc.",
                "Ticker": "AAPL",
                "Purchase price": 150.00,
                "Quantity": 10
              },
              {
                "Name": "Microhard Corporation",
                "Ticker": "MSFT",
                "Purchase price": 250.00,
                "Quantity": 5
              }
            ],
            "Last calculated risk scores": 0.3,
            "Max money to invest in this Portfolio": 5000.00,
            "Preferred risk for Portfolio": 0.6
          }
        }
      ]
    }
  }
# customer_data = next((customer for customer in st.session_state.get("CUSTOMER_JSON") if customer["Customer"]["Name"] == selected_customer), customer_data_alt)

if customer_data:
    st.write(f"Details for {selected_customer}:")
    
    # Iterate through the portfolios of the selected customer
    for portfolio in customer_data["Customer"]["Portfolio"]:            
            # Create an accordion (expander) for each portfolio
            with st.expander(portfolio["Portfolio Name"]):

                st.write("Stocks bought:")
                stocks_df = pd.DataFrame(portfolio["Portfolio item"]["Stocks bought"])
                st.table(stocks_df)

                # Create a DataFrame for the portfolio details
                st.write(f"Last calculated risk scores: {portfolio['Portfolio item']['Last calculated risk scores']}")


else:
    st.write("Customer not found or no portfolios available.")

if st.button("AI Generate Portfolio"):
    st.session_state["portfolio_page"] = "AI Generate Portfolio"
    st.experimental_rerun()