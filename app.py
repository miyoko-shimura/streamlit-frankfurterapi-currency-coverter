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

# Check if base and target currencies are the same
if base_currency == target_currency:
    st.write(f"{amount:.2f} {base_currency} is equal to {amount:.2f} {target_currency}")
else:
    # Frankfurter API endpoint
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={base_currency}&to={target_currency}"

    try:
        # Fetch data from the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()

        # Check if the response contains the expected data
        if "rates" in data and target_currency in data["rates"]:
            converted_amount = data["rates"][target_currency]
            # Display results in the main area
            st.write(f"{amount:.2f} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
        else:
            st.error("Unable to fetch conversion data. Please try again later.")

    except requests.RequestException as e:
        st.error(f"An error occurred while fetching data: {str(e)}")
    except KeyError as e:
        st.error(f"Unexpected data format received from the API. Error: {str(e)}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
