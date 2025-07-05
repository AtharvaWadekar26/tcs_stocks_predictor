# 📈 TCS Stock Price Predictor

A live Machine Learning-powered Flask web application that predicts the closing price of TCS (Tata Consultancy Services) stock based on user inputs like Open, High, Low, Volume, and Previous Close.

🔗 [Live App on Render](https://tcs-stocks-predictor.onrender.com/)

---

## 📊 Features

- 🔮 Predict closing price using Linear Regression
- 📥 Input fields: Open, High, Low, Volume, Previous Close
- 📈 Shows live market data for TCS using Yahoo Finance
- 🌐 Deployed on Render (Free cloud deployment)
- 💡 Built with Python, Flask, Pandas, Scikit-learn

---

## 🛠️ Tech Stack

| Tool            | Purpose                                |
|-----------------|----------------------------------------|
| Python          | Programming language                   |
| Flask           | Web framework                          |
| Pandas          | Data manipulation                      |
| Scikit-learn    | Machine learning (Linear Regression)   |
| yfinance        | Live stock data                        |
| Render.com      | Web deployment                         |
| HTML + CSS      | Frontend styling                       |

---

## 🚀 Screenshots

![image](https://github.com/user-attachments/assets/d41889c8-15c4-4f03-b735-c426be290388)


---

## 📁 Project Structure
TCS-StockApp/
├── app.py # Flask application
├── tcs_predict.py # Model + prediction logic
├── tcs_stock.csv # Training data (from MySQL or CSV)
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment config
└── templates/
└── predict.html # HTML interface

yaml
Copy
Edit

---

## 🧠 How It Works

1. `tcs_predict.py` loads and trains a Linear Regression model on historical stock data
2. User inputs values for Open, High, Low, Volume, and Prev Close
3. Model predicts the likely closing price
4. App also displays live TCS stock data using `yfinance`

---

## 📦 Setup Locally

```bash
git clone https://github.com/AtharvaWadekar26/tcs_stocks_predictor.git
cd tcs_stocks_predictor
pip install -r requirements.txt
python app.py

