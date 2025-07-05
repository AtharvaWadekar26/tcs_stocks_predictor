from flask import Flask, render_template, request
import tcs_predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    live_data = tcs_predict.get_live_stock_data()

    # Debug print
    print("FETCHED STOCK:", tcs_predict.get_live_stock_data())


    if request.method == 'POST':
        try:
            open_ = float(request.form['open'])
            high = float(request.form['high'])
            low = float(request.form['low'])
            volume = float(request.form['volume'])
            prev_close = float(request.form['prev_close'])

            predicted = tcs_predict.predict_price(open_, high, low, volume, prev_close)
            prediction = round(predicted, 2)
        except Exception as e:
            prediction = f"Invalid input. Error: {e}"

    return render_template("predict.html", prediction=prediction, live_data=live_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
