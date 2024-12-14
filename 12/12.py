import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# اضافه کردن یک ستون به یک دیتا فریم
# قطعه کد زیر ستون جدیدی به اسم new_columns با مقادیر 0 تا 25 به دیتا فریم اضافه میکند
df['new_columns']=[i for i in range(len(df))]
print(df)


# کد بالا تغیرات را روی دیتا فریم اصلی ایجاد میکند در حالی که دستور زیر دیتا فریم جدیدی ایجاد میکند 
df=df.assign(new=[i*3 for i in range(len(df))])
print(df)


