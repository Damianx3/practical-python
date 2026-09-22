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
                'name': row[0],
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

def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        row = (name, shares, current_price, change)
        report.append(row)
    return report

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}')
print('---------- ---------- ---------- ----------')

for name, shares, price, change in report:
    price_str = f'${price:.2f}'
    print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')