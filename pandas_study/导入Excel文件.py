import pandas as pd

df = pd.read_csv('总表.csv', index_col=0)
print(df)
print(df.columns.is_unique)
print(df['咨询日期'])
print(df.values)
print(df.describe())
