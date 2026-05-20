import pandas as pd

# 1. 使用「字典」建立 DataFrame
dict_data = {
    'Product': ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava'],
    'Price': [30, 20, 25, 60, 45, 35],
    'Sales': [100, 150, 80, 60, 90, 54]
}
df_dict = pd.DataFrame(dict_data)

# 2. 使用「列表（子列表）」建立 DataFrame
list_data = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df_list = pd.DataFrame(list_data, columns=['Product', 'Price', 'Sales'])

# 為了讓結果完全符合範例，我們以其中一個 DataFrame (df_dict) 繼續操作
df = df_dict

# 觀察資料前 5 筆與後 5 筆
print(df.head())
print(df.tail())

# 列數與欄數 (shape)
print(df.shape)

# 欄位名稱 (columns)
print(df.columns)

# 資料型態 (dtypes)
print(df.dtypes)

# 非空值數量 (count)
print(df.count())

# 數值欄位的統計資訊 (平均、標準差、極值與四分位數，取小數後2位)
stats = df.describe().round(2)
print(stats)

# 將統計資訊存檔為 0520_stock2.csv
stats.to_csv("0520_stock2.csv")