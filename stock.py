import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Analyzer")

col1, col2, col3 = st.columns(3)

with col1:
    stock_name = st.text_input("Enter the stock ticker: ", 'MSFT')

with col2:
    start_date = st.date_input("Enter the start date: ", datetime.date(2020, 1, 1))

with col3:
    end_date = st.date_input("Enter the end date: ", datetime.date(2024, 12, 13))

ticker_data = yf.Ticker(stock_name)

ticker_df = ticker_data.history(period = '1d', start = start_date, end = end_date)

st.subheader("Stock Information")
st.dataframe(ticker_df)

st.subheader("Stock Closing Price")
st.line_chart(ticker_df.Close)

st.subheader("Stock Volume")
st.line_chart(ticker_df.Volume)