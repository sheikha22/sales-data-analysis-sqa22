salesData = [
    {"product": "A", "sales": 50},
    {"product": "B", "sales": 80},
    {"product": "C", "sales": 30}
]

maxSales = 0
bestProduct = ""

 for product in salesData:
    if product["sales"] > maxSales:
        maxSales = product["sales"]
        bestProduct = product["product"]
    else:
        print("Sales value not higher than current maximum")


print("Best selling product:", bestProduct)
