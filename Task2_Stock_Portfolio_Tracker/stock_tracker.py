stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOG": 150,
    "AMZN": 200,
    "NFLX": 450
}

portfolio = {}
total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

print("\nAvailable Stocks:")
for stock in stocks:
    print(stock, ":", stocks[stock])

print("\nEnter QUIT to finish.\n")

while True:

    stock_name = input("Enter Stock Name: ").upper()

    if stock_name == "QUIT":
        break

    if stock_name not in stocks:
        print("Stock not available!")
        continue

    quantity = int(input("Enter Quantity: "))

    if stock_name in portfolio:
        portfolio[stock_name] = portfolio[stock_name] + quantity
    else:
        portfolio[stock_name] = quantity

    print("Stock Added Successfully!\n")

print("\n===== PORTFOLIO SUMMARY =====")

print("Stock\tQuantity\tPrice\tValue")

for stock in portfolio:

    quantity = portfolio[stock]
    price = stocks[stock]
    value = quantity * price

    total = total + value

    print(stock, "\t", quantity, "\t\t", price, "\t", value)

print("\nTotal Investment Value =", total)