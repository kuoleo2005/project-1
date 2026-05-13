import numpy as np
import csv

products, price, stock, discount = [], [], [], []

with open("Stock_1.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        products.append(row["Product"])
        price.append(float(row["Price"]))
        stock.append([float(row["Stock_A"]), float(row["Stock_B"]), float(row["Stock_C"])])
        discount.append(float(row["Discount"]))

products = np.array(products)
price = np.array(price)
stock = np.array(stock)
discount = np.array(discount)

total_stock = stock.sum(axis=1)
total_value = price * total_stock
discount_price = price * discount

# 優化：改用陣列條件比對，避免 argmax 漏抓並列第一的商品
is_hot = (total_stock == total_stock.max())
is_low = (total_stock == total_stock.min())

with open("Stock_OK.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Product", "Stock", "Value", "Discount", "Hot", "Low"])

    for i in range(len(products)):
        w.writerow([
            products[i],
            total_stock[i],
            total_value[i],
            discount_price[i],
            is_hot[i],
            is_low[i]
        ])