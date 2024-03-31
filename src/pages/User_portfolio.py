import streamlit as st


st.set_page_config(page_title="User Portfolio")

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

if st.button("AI Generate Portfolio"):
    st.session_state["portfolio_page"] = "AI Generate Portfolio"
    st.experimental_rerun()