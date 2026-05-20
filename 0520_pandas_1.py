import pandas as pd

# 1. 建立資料與索引
data = [120, 80, None, 60, 95, None, 110]
idx = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']

# 2. 建立 stock1 (預設數字索引) 與 stock2 (自訂文字索引)
stock1 = pd.Series(data)
stock2 = pd.Series(data, index=idx)

# 3. 轉為字典
stock3 = stock2.to_dict()

# 4. 依序輸出結果
print("stock1")
print(stock1)

print("\nstock2")
print(stock2)

print("\nstock3")
print(stock3)

print(f"\nBanana 庫存： {stock2['Banana']}")

print("\n缺失值檢查：")
print(stock2.isna())

print(f"\n缺失值數量： {stock2.isna().sum()}")

# 5. 將 stock2 存為 CSV 檔案
stock2.to_csv("0520_stock.csv", header=False)