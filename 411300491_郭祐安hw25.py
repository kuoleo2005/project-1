import pandas as pd

df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset.csv")

df['Unit_Price'] = df['Unit_Price'].astype(str).str.replace('$', '').str.strip().astype(float)

df['Total_Inventory_Value'] = df['Stock_Quantity'] * df['Unit_Price']

best_selling_product = df.loc[df['Sales_Volume'].idxmax()]

df['Discounted_Revenue'] = df['Sales_Volume'] * df['Unit_Price'] * 0.9

print("=== (1) 總庫存價值 & (3) 9折後收入 (顯示前5筆) ===")
print(df[['Product_Name', 'Total_Inventory_Value', 'Discounted_Revenue']].head())

print("\n=== (2) 最暢銷商品 ===")
print("商品名稱:", best_selling_product['Product_Name'])
print("銷售量:", best_selling_product['Sales_Volume'])