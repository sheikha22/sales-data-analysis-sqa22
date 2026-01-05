 count = 0

for product in salesData:
    count += 1   # تعديل داخل loop
    if product["sales"] > maxSales:
        maxSales = product["sales"]
        bestProduct = product["product"]
    else:
        bestProduct = bestProduct

