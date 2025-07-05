import pandas as pd
from sklearn.linear_model import LinearRegression
import yfinance as yf

# 🔄 Load model from CSV
def load_model():
    try:
        df = pd.read_csv("tcs_stock.csv")
        print("📊 Loaded rows from CSV:", len(df))

        # Clean column names (remove spaces, lowercase)
        df.columns = df.columns.str.strip().str.capitalize()

        df['Prev_close'] = df['Close'].shift(1)
        df.dropna(inplace=True)
        print("✅ Rows after dropna:", len(df))

        if len(df) == 0:
            print("⚠️ No usable data after dropna. Cannot train model.")
            return None

        X = df[['Open', 'High', 'Low', 'Volume', 'Prev_close']]
        y = df['Close']

        model = LinearRegression()
        model.fit(X, y)
        return model
    except Exception as e:
        print("❌ Error loading model:", e)
        return None

# Load model once globally
model = load_model()

# 🔍 Predict closing price from inputs
def predict_price(open_, high, low, volume, prev_close):
    if model is None:
        return "⚠️ Model not trained due to lack of data."

    input_data = [[open_, high, low, volume, prev_close]]
    return round(model.predict(input_data)[0], 2)

# 📈 Fetch live TCS stock data using yfinance
def get_live_stock_data(ticker="TCS.NS"):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")

        if data.empty:
            print("⚠️ No live stock data found.")
            return None

        last_row = data.iloc[-1]
        return {
            "Open": round(last_row['Open'], 2),
            "High": round(last_row['High'], 2),
            "Low": round(last_row['Low'], 2),
            "Close": round(last_row['Close'], 2),
            "Volume": int(last_row['Volume']),
        }
    except Exception as e:
        print("❌ Error fetching live stock data:", e)
        return None
