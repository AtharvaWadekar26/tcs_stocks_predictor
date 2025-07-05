import pandas as pd
import mysql.connector
from sklearn.linear_model import LinearRegression

def load_model():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Athu@2608",  # replace with your real password
        database="tcs_stock_analysis"
    )
    df = pd.read_sql("SELECT * FROM tcs_stock", conn)
    conn.close()

    df['Prev_Close'] = df['Close'].shift(1)
    df = df.dropna()

    X = df[['Open', 'High', 'Low', 'Volume', 'Prev_Close']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    return model

model = load_model()  # Load once globally

def predict_price(open_, high, low, volume, prev_close):
    input_data = [[open_, high, low, volume, prev_close]]
    return model.predict(input_data)[0]

import yfinance as yf

def get_live_stock_data(ticker="TCS.NS"):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")

        if data.empty:
            return None

        last_row = data.iloc[-1]
        return {
            "Open": round(last_row['Open'], 2),
            "High": round(last_row['High'], 2),
            "Low": round(last_row['Low'], 2),
            "Close": round(last_row['Close'], 2),
            "Volume": int(last_row['Volume']),
        }
    except:
        return None

