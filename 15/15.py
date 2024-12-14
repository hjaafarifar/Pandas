import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# حذف یک سطر از دیتا فریم

df.drop(5,axis='rows',inplace=True)
print(df)
# 5 در کد بالا شماره اندیس سطری است که میخواهیم خذف شود
# اتریبوت inplace در کد بلا تغیرات را روی دیتا فریم اصلی ایجاد میکند
