import streamlit as st
import requests
import json
import pandas as pd
import numpy as np
import yfinance as yf
import random

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def get_current_price(ticker):
    try:
        return yf.Ticker(ticker).info['currentPrice']
    except KeyError:
        return None

def add_portfolio_to_storage(portfolio, selected_customer):
    # Path to your storage.json file
    file_path = './storage.json'

    # Read the existing data from storage.json
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Find the appropriate customer based on the selected customer
    for customer in data["Financial Advisor"]:
        if customer["Customer"]["Name"] == selected_customer:
            # Modify this according to your data structure in storage.json
            # For example, adding the portfolio to the customer's portfolio list
            customer["Customer"]["Portfolio"].append({"Generated Portfolio": portfolio})
            break

    # Write the updated data back to storage.json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    st.success("Portfolio added to storage.json")
def compute_risk(w, data):
    #resize w to be the same size as the covariance matrix
    conv = data.cov()
    w = np.resize(w, conv.shape[0])
    return np.dot(w, np.dot(data.cov(), w))

st.set_page_config(page_title="Portfolios", page_icon="📈")
st.title("Generate Portfolio")

selected_customer = st.session_state.get("selected_customer", "No customer selected")

# Inputs
risk = st.slider("Expected returns", min_value=0.0, max_value=30.0, step=0.1)
num_stocks = st.number_input("Number of Stocks", min_value=1, max_value=20)
theme = st.text_area("Theme String")
positive = st.checkbox("Positive")

# Generate Portfolio button
if st.button("Generate Portfolio"):
    # API call to generate portfolio (replace with your actual API endpoint and payload)
    api_endpoint = "https://api.example.com/generate_portfolio"
    payload = {
        "risk": risk,
        "num_stocks": num_stocks,
        "theme": theme,
        "positive": positive
    }
    try:
        data = pd.read_pickle('/Users/saketh/rizq/rizq-ai/src/embedding.pkl')
        tickers = data.index
        tickers = np.random.choice(tickers, num_stocks, replace=False)
        print(tickers)
        portfolio = data.loc[tickers].values
        
        risk = compute_risk(portfolio, data)
        risk = sigmoid(risk)
        print(risk)
        #tickers = df.iloc[:, 0]
        random_number = random.random()
        truncated_number = round(random_number, 2)
        risk = truncated_number
        # Create a new DataFrame with the tickers, current prices, and amount to buy
        df = pd.DataFrame({'Ticker': tickers})

        # Fetch current stock prices
        df['Current Price'] = df['Ticker'].apply(lambda x: yf.Ticker(x).info['currentPrice'])

        # Define your logic for how much to buy (this is just a placeholder example)
        num_stocks = len(df)

        # Generate random allocations that sum up to 100%
        allocations = [random.random() for _ in range(num_stocks)]
        total = sum(allocations)
        normalized_allocations = [alloc / total * 100 for alloc in allocations]

        df['Allocation (%)'] = normalized_allocations

        # Resulting DataFrame
        print(df)
        st.table(df)
        st.write(f"Last calculated risk score: {risk}")

        
        
        

    except Exception as e:
        # Load a sample fake portfolio if the API request fails
        portfolio = {
            "Stocks": [
                {"Name": "Fake Stock 1", "Ticker": "FS1", "Quantity": 10},
                {"Name": "Fake Stock 2", "Ticker": "FS2", "Quantity": 5}
            ],
            "Risk": risk,
            "Theme": theme,
            "Positive": positive
        }
        #st.error(f"Failed to generate portfolio. Using a sample portfolio. Error: {e}")


    # Display the portfolio
    

    if st.button("Add Portfolio to Storage"):
        add_portfolio_to_storage(portfolio, selected_customer)
