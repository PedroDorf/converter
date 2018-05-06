#!/usr/bin/python3
import sys, json
from getopt import getopt, GetoptError
from conv import convert


def loadInput(argv):
    try:
        opts, args = getopt(argv, "", ["amount=", "input_currency=", "output_currency="])
    except GetoptError:
        sys.exit("Options are incorrect.")

    fromCurrency, toCurrency, amount = ("", "", 0)

    for el in opts:
        if el[0] == "--amount":
            amount = el[1]
        elif el[0] == "--input_currency":
            fromCurrency = el[1]
        elif el[0] == "--output_currency":
            toCurrency = el[1]
    amount = float(amount)
    return fromCurrency, toCurrency, amount


def main(argv):
    fromCurrency, toCurrency, amount = loadInput(argv)
    output = convert(fromCurrency, toCurrency, amount)
    if output is None:
        sys.exit("Something went wrong. Please try later or contact IT support.")
    with open("outputFile.json", "w") as file:
        json.dump(output, file, indent=4, sort_keys=True)


if __name__ == "__main__":
    main(sys.argv[1:])