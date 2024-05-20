import streamlit as st
import numpy as np;
import pandas as pd;
import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve page with status code: {response.status_code}")
        return None

def parse_trending_stocks(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'W(100%)'})
    if not table:
        print("Failed to find the trending stocks table.")
        return []

    rows = table.find_all('tr')
    trending_stocks = []

    for row in rows[1:]:
        columns = row.find_all('td')
        if len(columns) < 2:
            continue
        symbol = columns[0].text.strip()
        name = columns[1].text.strip()
        trending_stocks.append((symbol, name))

    return trending_stocks

url = 'https://finance.yahoo.com/trending-tickers'

html = get_html(url)
stock_list = []
if html:
    trending_stocks = parse_trending_stocks(html)
    df = pd.DataFrame(trending_stocks, columns=['Symbol', 'Name'])
    st.header("Trending Stocks")
    # Adjust display settings for the DataFrame
    st.dataframe(df, width=1000, height=600)        
    for stock in trending_stocks:
        stock_list.append(stock[0])

# import pandas as pd
# import yfinance as yf
# import seaborn as sns
# import matplotlib.pyplot as plt

# # List of NIFTY 50 ticker symbols
# nifty_50_tickers = [
#     'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS',
#     'ICICIBANK.NS', 'KOTAKBANK.NS', 'HDFC.NS', 'ITC.NS', 'SBIN.NS',
#     'BHARTIARTL.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJFINANCE.NS',
#     'LT.NS', 'ULTRACEMCO.NS', 'MARUTI.NS', 'TITAN.NS', 'M&M.NS',
#     'BAJAJFINSV.NS', 'SUNPHARMA.NS', 'NESTLEIND.NS', 'POWERGRID.NS',
#     'HCLTECH.NS', 'WIPRO.NS', 'GRASIM.NS', 'ADANIGREEN.NS', 'NTPC.NS',
#     'TATASTEEL.NS', 'JSWSTEEL.NS', 'DIVISLAB.NS', 'DRREDDY.NS',
#     'BPCL.NS', 'BRITANNIA.NS', 'HEROMOTOCO.NS', 'CIPLA.NS', 'INDUSINDBK.NS',
#     'TECHM.NS', 'SHREECEM.NS', 'TATAMOTORS.NS', 'UPL.NS', 'COALINDIA.NS',
#     'BAJAJ-AUTO.NS', 'IOC.NS', 'ONGC.NS', 'HINDALCO.NS', 'VEDL.NS', 'ADANIPORTS.NS',
#     'SBILIFE.NS', 'EICHERMOT.NS'
# ]

# # Fetch data from yfinance
# data = yf.download(nifty_50_tickers, start='2023-01-01', end='2023-12-31')['Adj Close']

# # Calculate daily returns
# returns = data.pct_change().dropna()

# # Calculate correlation matrix
# correlation_matrix = returns.corr()

# # Create heatmap
# plt.figure(figsize=(15, 10))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Correlation Heatmap of NIFTY 50 Stocks (2023)')
# plt.show()













