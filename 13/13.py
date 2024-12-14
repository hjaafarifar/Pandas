import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# حذف کردن یک ستون از دیتا فیرم
# کد زیر با اتریبیوت inplace تغیرات را روی دیتا فریم اصلی ایجاد میکند
df.drop('top_speed',axis=1,inplace=True)
print(df)
