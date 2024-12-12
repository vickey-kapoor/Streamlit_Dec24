import streamlit as st
import yfinance as yf

st.title("Stock Analyzer.")

ticker_data = yf.Ticker("MSFT")

ticker_df = ticker_data.history(period = '1d', start = '2020-01-01', end = '2023-12-31')

st.dataframe(ticker_df)