from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates

app = Flask(__name__)
c = CurrencyRates()


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    currencies = ['USD', 'EUR', 'RUB', 'JPY', 'CNY', 'GBP', 'TRY']

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_curr = request.form['from_curr'].upper()
            to_curr = request.form['to_curr'].upper()

            if from_curr == to_curr:
                raise ValueError("Выберите разные валюты")

            converted_amount = c.convert(from_curr, to_curr, amount)
            result = f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}"

        except Exception as e:
            result = f"Ошибка: {str(e)}"

    return render_template('index.html',
                           result=result,
                           currencies=currencies)


if __name__ == '__main__':
    app.run(debug=True)