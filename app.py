import streamlit as st
import requests

st.title("Frankfurter API Currency Converter")

# Input fields
amount = st.text_input("Amount", value="1.00")
try:
    amount = float(amount)
    if amount < 0:
        st.error("Please enter a non-negative amount.")
except ValueError:
    st.error("Please enter a valid number.")
base_currency = st.selectbox("From", ["USD", "GBP", "EUR", "JPY"])
target_currency = st.selectbox("To", ["JPY", "EUR", "GBP", "USD"])

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

st.write("---")
st.write("Acknowledgements: Exchange rates provided by the [Frankfurter API](https://www.frankfurter.app/). ")
st.write("")

st.warning(
    """
    **Legal Disclaimer**
     
    The information provided by this currency converter is for general informational purposes only. 
    While we strive to keep the information up to date and correct, we make no representations or 
    warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, 
    or availability with respect to the currency converter or the information, products, services, or related 
    graphics contained in the currency converter for any purpose. Any reliance you place on such information 
    is therefore strictly at your own risk.
    
    In no event will we be liable for any loss or damage including without limitation, indirect or consequential 
    loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in 
    connection with, the use of this currency converter.
    
    This application uses the Frankfurter API to retrieve currency exchange rates. The application is provided 
    in accordance with the terms of use of the Frankfurter API. The provider of the Frankfurter API shall not be 
    liable for any damages arising from the use of the API.
    """
)
