import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="7d")  # Fetch data for the past 7 days
    return hist

def calculate_percent_change(data):
    data['Percent Change'] = data['Close'].pct_change() * 100
    return data

def plot_heatmap(data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, fmt=".2f", cmap="RdYlGn", cbar=True)
    plt.title('Stock Price Percent Change Heatmap')
    st.pyplot(plt)

st.title("Stock Price Percent Change Heatmap")

tickers = ['IRFC.NS', 'SBIN.NS', 'ACC.NS','ADANIENT.NS', 'AWL.NS', 'FORTIS.NS']


percent_changes = {}

for ticker in tickers:
    data = fetch_stock_data(ticker)
    data = calculate_percent_change(data)
    percent_changes[ticker] = data['Percent Change']

# Convert to DataFrame for heatmap
percent_changes_df = pd.DataFrame(percent_changes)
st.write("Stock Percent Changes Data:")
st.write(percent_changes_df)

# Plot heatmap
plot_heatmap(percent_changes_df.T)


percent_changes_ = {}
selected_stock = st.text_input("label goes here", 'GOOG')
data_ = fetch_stock_data(selected_stock)
data_ = calculate_percent_change(data_)
percent_changes_[selected_stock] = data_['Percent Change']
percent_changes_df_ = pd.DataFrame(percent_changes_)
st.write("Stock Percent Changes Data:")
st.write(percent_changes_df_)
plot_heatmap(percent_changes_df_.T)