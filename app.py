from flask import Flask, request, jsonify
from flask_api import status
from conv import convert

app = Flask(__name__)


@app.route("/currency_converter")
def index():
    fromCurrency = request.args.get('input_currency', '')
    toCurrency = request.args.get('output_currency', '')
    try:
        amount = float(request.args.get('amount', ''))
    except ValueError:
        return "Cannot convert amount to float.", status.HTTP_400_BAD_REQUEST
    if fromCurrency == "":
        return "Input currency is missing.", status.HTTP_400_BAD_REQUEST

    return jsonify(convert(fromCurrency, toCurrency, amount))

if __name__ == '__main__':
    app.run()