import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="Real-Time Currency Converter")

# Sidebar header
st.sidebar.header("Currency Converter")

# Input fields in the sidebar
base_currency = st.sidebar.selectbox("From", ("USD", "EUR", "GBP", "JPY"))
target_currency = st.sidebar.selectbox("To", ("USD", "EUR", "GBP", "JPY"))
amount = st.sidebar.number_input("Amount", min_value=1.00)

# Frankfurter API endpoint
url = f"https://api.frankfurter.app/latest?amount={amount}&from={base_currency}&to={target_currency}"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Extract converted amount
converted_amount = data["rates"][target_currency]

# Display results in the main area
st.write(f"{amount:.2f} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
