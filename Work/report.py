# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'names': row[0],
                'shares': int(row[1]),
                'price': float(row[2]),
            }
            portfolio.append(holding)
        return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
        return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
total_value = 0.0

for stock in portfolio:
    total_cost += stock['shares'] * stock['price']
    total_value += stock['shares'] * prices[stock['name']]

