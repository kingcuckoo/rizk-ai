

# AI-Driven Financial Portfolio Generator

## Overview
This application is designed to assist financial advisors in creating customized investment portfolios for their clients. By leveraging artificial intelligence, the app provides an intuitive interface for generating portfolios based on various parameters such as risk tolerance, number of stocks, and investment themes. Additionally, users can manually build portfolios, with all data being stored for future reference.

## Features
- **Customer Selection**: Choose a client from a predefined list to view or create portfolios.
- **Portfolio Details**: View detailed information about each portfolio, including stock allocations, risk scores, and investment limits.
- **AI Generate Portfolio**: Automatically generate a portfolio based on user-defined criteria such as risk level, number of stocks, and investment theme.
- **Manual Build Portfolio**: Manually create a portfolio with custom stock selections and allocations.
- **Data Storage**: All portfolio information is stored in a JSON file for easy retrieval and management.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/financial-portfolio-generator.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. **Select a Customer**: Start by selecting a customer from the dropdown menu on the "Select Customer" page.
2. **View Portfolio Details**: Navigate to the "Customer Details" page to view existing portfolios for the selected customer.
3. **Generate a New Portfolio**:
   - Go to the "AI Generate Portfolio" page.
   - Set the desired risk level, number of stocks, and investment theme.
   - Optionally, choose whether the portfolio should have a positive or negative outlook.
   - Click "Generate Portfolio" to create a new portfolio based on the specified criteria.
   - Review the generated portfolio and click "Add Portfolio to Storage" to save it.
4. **Manually Build a Portfolio**: On the "Manual Build Portfolio" page, you can manually add stocks and their allocations to create a custom portfolio.
