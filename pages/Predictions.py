import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd;
import matplotlib.pyplot as plt;
import streamlit as st
from plotly import graph_objs as go


START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Predictions')



sp500_url = "https://en.wikipedia.org/wiki/NIFTY_500"
tables = pd.read_html(sp500_url)
sp500_table = tables[2]

sp500_tickers = sp500_table[3].tolist()
sp500_tickers.remove('Symbol')
for i in range(len(sp500_tickers)):
    sp500_tickers[i] = sp500_tickers[i] + ".BO"


# stocks = ('GOOG', 'AAPL', 'MSFT', 'GME', 'HOOD')
# # selected_stock = 'GOOG'
# selected_stock = st.text_input("label goes here", 'GOOG')
# # selected_stock = st.selectbox('Select dataset for prediction', sp500_tickers)
# n_years = st.slider('Years of prediction:', 1, 4)
# period = n_years * 365

# def load_data(ticker):
#     data = yf.download(ticker, START, TODAY)
#     data.reset_index(inplace=True)
#     return data




stocks = ('GOOG', 'AAPL', 'MSFT', 'GME', 'HOOD')
# selected_stock = 'GOOG'
selected_stock = st.text_input("label goes here", 'GOOG')
# selected_stock = st.selectbox('Select dataset for prediction', sp500_tickers)
n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
df = yf.download(selected_stock, start=START, end=TODAY)
data_load_state.text('Loading data... done!')

if df.empty:
    st.error("No data found for the given ticker. Please check the ticker symbol and try again.")
else:
    st.subheader("Data from 2020 - 2024")
    st.write(df.describe())
    st.subheader("closing Price vs Time chart")
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Closing Price'))
    fig = go.Figure()

   
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Closing Price'))


    fig.update_layout(title=f"{selected_stock} Stock Trend", xaxis_title='Date', yaxis_title='Price')
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)


    st.subheader("Candlestick Chart")
    fig_candlestick = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Candlestick'
    )])
    fig_candlestick.update_layout(
        title=f"{selected_stock} Candlestick Chart",
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False
    )
    st.plotly_chart(fig_candlestick)







    st.plotly_chart(fig)
    st.subheader("Closing Price vs Time chart with 100MA")
    df['100MA'] = df['Close'].rolling(window=100).mean()
    ma100 = df['100MA'] 
    fig.add_trace(go.Scatter(x=df.index, y=df['100MA'], mode='lines', name='100-day Moving Average'))
    fig.update_layout(title=f"{selected_stock} Stock Trend", xaxis_title='Date', yaxis_title='Price')
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)







    st.subheader("Closing Price vs Time chart with 100MA & 200MA")
    df['100MA'] = df['Close'].rolling(window=100).mean()
    df['200MA'] = df['Close'].rolling(window=200).mean()
    ma100 = df['100MA']
    
    fig.add_trace(go.Scatter(x=df.index, y=df['200MA'], mode='lines', name='200-day Moving Average'))

    fig.update_layout(title=f"{selected_stock} Stock Trend with Moving Averages",xaxis_title='Date', yaxis_title='Price')
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)



    df_train = data[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.subheader('Forecast data')
    st.write(forecast.tail())
        
    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)
