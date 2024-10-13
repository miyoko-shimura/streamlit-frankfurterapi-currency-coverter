import streamlit as st
import requests

st.title("Frankfurter API Currency Converter")

# Input fields
amount = st.number_input("Amount", min_value=0.01, value=1.00, step=0.01)
base_currency = st.selectbox("From", ["USD", "EUR", "GBP", "JPY"])
target_currency = st.selectbox("To", ["EUR", "GBP", "JPY", "USD"])

# Convert button
if st.button("Convert"):
    if base_currency == target_currency:
        st.write(f"{amount:.2f} {base_currency} = {amount:.2f} {target_currency}")
    else:
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={base_currency}&to={target_currency}"
        try:
            response = requests.get(url)
            data = response.json()
            if "rates" in data and target_currency in data["rates"]:
                result = data["rates"][target_currency]
                st.write(f"{amount:.2f} {base_currency} = {result:.2f} {target_currency}")
            else:
                st.error("Unable to fetch conversion data. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
