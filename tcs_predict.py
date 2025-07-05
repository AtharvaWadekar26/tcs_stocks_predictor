import pandas as pd
from sklearn.linear_model import LinearRegression
import yfinance as yf

def load_model():
    # Load data from the local CSV file
    df = pd.read_csv("tcs_stock.csv")
    df['Prev_Close'] = df['Close'].shift(1)
    df.dropna(inplace=True)

    X = df[['Open', 'High', 'Low', 'Volume', 'Prev_Close']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)
    return model

model = load_model()

def predict_price(open_, high, low, volume, prev_close):
    input_data = [[open_, high, low, volume, prev_close]]
    return model.predict(input_data)[0]

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
