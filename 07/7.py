import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# نمایش تعداد سطر و ستون به صورت یک tuple
print(df.shape,'\n',100*'*')

# تعداد سطر ها را برمیگرداند
print(len(df),'\n',100*'*')

# یک ستون را گرفته تعداد داده هایی که nan نیستند را نمایش میدهد
print(df['min_speed'].count(),'\n',100*'*')

# دستورات زیر کوچک ترین بزرگترین و میانه یک ستون را محاسبه میکنند
print(df['top_speed'].min())
print(df['top_speed'].max())
print(df['top_speed'].mean(),'\n',100*'*')

# دستور زیر مقادیر آماری تمام ستون هایی که عدد هستند را برمیگرداند
print(df.describe())