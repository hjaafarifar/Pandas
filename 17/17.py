import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# not a number=nan در یک دیتا فریم
# برسی میکند کدام ستون ها nan دارند
print(df.isna())
print(df.isna().sum())# مقدار کمی هر ستون را مشخص میکند

# خذف nan ها در یک دیتا فریم
# df.dropna(inplace=True)
# print(df)

# پر کردن جای nan در یک دیتا فریم
df.fillna(15,inplace=True)
print(df)