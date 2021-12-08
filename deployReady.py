import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
import csv
import datetime
###########
# sidebar #
###########

stockChoice = []

with open('./resources/nasdaq_screener_1638830312199.csv') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
         stockChoice.append(row[0])
print(stockChoice)

stock = st.sidebar.text_input('Chose a stock to predict', "TSLA")
stockFav = st.sidebar.selectbox('Favourites', stockChoice)

option = st.sidebar.selectbox('Choose a time period', ('Year', 'Month', 'Week'))

Start = "2015-01-01"
Today = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")

period = 0
if option == "Year":
    n_days = st.sidebar.slider("Years to predict:", 1, 5)
    period = n_days * 365
if option == "Month":
    n_days = st.sidebar.slider("Months to predict:", 1, 5)
    period = n_days * 12
if option == "Week":
    n_days = st.sidebar.slider("Weeks to predict:", 1, 5)
    period = n_days * 7
else:
    print("Error. Please select Year, Month, or Week")


#
##n_days = st.slider(option, 1, 5)
# period = n_days * 365


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
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text='Time serious Data', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()

# Forecast
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data for', option)
st.write(forecast.tail())

st.write("forecast data for", option)
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast Component')
fig2 = m.plot_components(forecast)
st.write(fig2)
