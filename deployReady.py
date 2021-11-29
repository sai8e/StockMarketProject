# 
import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go 



Start = "2015-01-01"
Today = date.today().strftime("%Y-%m-%d")



st.title("Stock Prediction App")


stock = st.text_input("Choose a Stock to Predict", "TSLA")
#stocks = ("AAPL", "GOOG", "MSFT", "GME")
#selected_stock = st.selectbox("Select dataset for prediction", stocks)

n_days = st.slider("Years to predict:",1 , 5)
period = n_days *365


@st.cache
def load_data(ticker):
    data = yf.download(ticker, Start, Today)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data...")
data = load_data(stock)
data_load_state.text("Loading data...Done")

st.subheader('Raw Data')
st.write(data.tail())

def plot_raw_data():
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=data['Date'],y = data['Open'],name = 'stock_open'))
  fig.add_trace(go.Scatter(x=data['Date'],y = data['Close'],name = 'stock_close'))
  fig.layout.update(title_text='Time serious Data', xaxis_rangeslider_visible=True)
  st.plotly_chart(fig)

plot_raw_data()

# Forecast
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())


st.write("forecast data")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast Component')
fig2 = m.plot_components(forecast)
st.write(fig2)
