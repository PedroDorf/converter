import json
import requests


def convertToStandard(string):
    if string is None:
        return None
    with open("currencyStandards.json", "r") as file:
        symbols = json.load(file)
    for element in symbols:
        if symbols[element]["symbol"] == string or element == string:
            return element
    return None


def getRates(currency):
    url = "https://v3.exchangerate-api.com/bulk/9c126d038ec279cb6c453456/" + currency
    response = requests.get(url)
    rates = response.json()
    return rates["rates"]


def convertToAllCurrencies(currency, amount):
    rates = getRates(currency)
    for el in rates:
        rates[el] *= amount
    return rates


def findRate(fromCurrency, toCurrency):
    rates = getRates(fromCurrency)
    return rates[toCurrency]


def convert(fromCurrency, toCurrency, amount):
    result = {}
    toCurrency = convertToStandard(toCurrency)
    fromCurrency = convertToStandard(fromCurrency)
    result["input"] = {"amount": amount, "currency": fromCurrency}
    if fromCurrency is None:
        print("Unknown input currency type.")
        return None
    if toCurrency is None:
        result["output"] = convertToAllCurrencies(fromCurrency, amount)
    else:
        rate = findRate(fromCurrency, toCurrency)
        result["output"] = {toCurrency: amount*rate}
    return result
