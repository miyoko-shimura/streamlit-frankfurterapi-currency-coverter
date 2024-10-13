# Streamlit Frankfurter API Currency Coverter

A simple and efficient currency converter built with Streamlit and powered by the Frankfurter API.
Features

🌐 Real-time currency conversion
💱 Support for USD, EUR, GBP, and JPY
🚀 Fast and responsive interface
🛠 Easy-to-use Streamlit app

Installation

Clone this repository:
Copygit clone https://github.com/yourusername/frankfurter-api-currency-converter.git

Navigate to the project directory:
Copycd frankfurter-api-currency-converter

Install the required packages:
Copypip install -r requirements.txt


Usage

Run the Streamlit app:
Copystreamlit run app.py

Open your web browser and go to http://localhost:8501.
Enter the amount you want to convert, select the base currency and target currency, then click "Convert".

Code Overview
pythonCopyimport streamlit as st
import requests

st.title("Frankfurter API Currency Converter")

# Input fields
amount = st.number_input("Amount", min_value=0.01, value=1.00, step=0.01)
base_currency = st.selectbox("From", ["USD", "EUR", "GBP", "JPY"])
target_currency = st.selectbox("To", ["EUR", "GBP", "JPY", "USD"])

# Convert button
if st.button("Convert"):
    # Conversion logic here...
Dependencies

Streamlit
Requests

API Used
This app uses the Frankfurter API for currency conversion rates.
Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.
License
MIT
Contact
Your Name - @yourtwitter - email@example.com
Project Link: https://github.com/yourusername/frankfurter-api-currency-converter
