import yfinance as yf
import streamlit as st

st.write("""
# Simple stock price app

Shown are the stock **closing price** and **volume** of ***Apple Inc.***!
""")
# define the ticker symbol
tickerSymbol = 'AAPL'
# get data on thi,s ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(
    period='1d', start='2011-05-31', end='2021-05-31')
# Open   High   Low   Close   Volume   Dividends   Stock   Splits

st.write("""
## Closing Price ($)
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
