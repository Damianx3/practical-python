# pcost.py
#
# Exercise 1.27
total = 0.0

f = open('Data/portfolio.csv', 'rt')

# Skip the header row
next(f)

for line in f:
    row = line.split(',')

    shares = int(row[1])
    price = float(row[2])

    cost = shares * price
    total = total + cost

f.close()

print('Total cost', total)