import streamlit as st
import openai
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.title('Real-time Stock Market Data Analysis with Azure OpenAI GPT')

# Create a text input for entering the stock symbol
stock_symbol = st.text_input('Enter a stock symbol (e.g., AAPL)')

# Set up Azure OpenAI GPT
# Set up Azure OpenAI GPT
# Authenticate with OpenAI API
openai.api_type = "azure"
openai.api_base = 'https://testgpt9212.openai.azure.com/'
openai.api_version = "2023-03-15-preview"
#openai.api_key = 'xxxxxxxxxxxxxxxxxxxxx'
openai.api_key = st.secrets['path']
#model_engine = "code-davinci-002"
gpt_model = "text-davinci-003"  # Azure OpenAI GPT model

# Create a function to generate a textual summary using Azure OpenAI GPT
def generate_summary(symbol, data):
    # Implement your logic to generate the summary using Azure OpenAI GPT
    # You can analyze the stock market data and generate a summary based on the trends, news, or other factors

    # Example placeholder logic:
    summary = f"This is a summary for stock symbol {symbol}. The stock has shown an upward trend in the recent days, driven by positive news about a new product launch. Analysts are optimistic about the future performance of the stock. However, it is important to note that stock market trends are subject to change based on various factors."
    return summary

if stock_symbol:
    # Load stock data
    stock_data = yf.download(stock_symbol)

    if not stock_data.empty:
        # Display the stock data
        st.subheader('Stock Data')
        st.write(stock_data.tail())

        # Generate textual summary using Azure OpenAI GPT
        if st.button('Generate Summary'):
            # Perform text generation using Azure OpenAI GPT
            summary_text = generate_summary(stock_symbol, stock_data)

            # Display the generated summary
            st.subheader('Generated Summary')
            st.write(summary_text)

        # Visualize the stock data
        st.subheader('Stock Data Visualization')
        plt.figure(figsize=(10, 6))
        plt.title(f'{stock_symbol} Stock Price')
        plt.plot(stock_data['Close'])
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        st.pyplot(plt)

        # Perform analysis on the stock data
        st.subheader('Stock Data Analysis')

        # Calculate and display the simple moving average (SMA)
        sma_period = st.slider('Select SMA period', min_value=5, max_value=50, value=20)
        stock_data['SMA'] = stock_data['Close'].rolling(sma_period).mean()
        st.write(stock_data.tail())

        # Calculate and display the moving average convergence divergence (MACD)
        exp_short = st.slider('Select MACD exponential moving average (short)', min_value=5, max_value=20, value=12)
        exp_long = st.slider('Select MACD exponential moving average (long)', min_value=21, max_value=50, value=26)
        exp_signal = st.slider('Select MACD exponential moving average (signal)', min_value=5, max_value=20, value=9)
        stock_data['EMA_short'] = stock_data['Close'].ewm(span=exp_short, adjust=False).mean()
        stock_data['EMA_long'] = stock_data['Close'].ewm(span=exp_long, adjust=False).mean()
        stock_data['MACD'] = stock_data['EMA_short'] - stock_data['EMA_long']
        stock_data['Signal'] = stock_data['MACD'].ewm(span=exp_signal, adjust=False).mean()
        st.write(stock_data.tail())

    else:
        st.warning('Stock data not found. Please enter a valid stock symbol.')
