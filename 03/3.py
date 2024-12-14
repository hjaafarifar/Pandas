import pandas as pd
from pathlib import Path
# استفاده از ماژول pathlib برای دسترسی به داده
mypath=Path('../pandas')

df=pd.read_csv(mypath/'data.txt')

# دسترسی به ستون های یک دیتا فریم
print(df.columns)

print(40*'*')
# دسترسی به مقادیر یک دیتا فریم
print(df.values)

print(40*'*')
# دسترسی به اندیس های یک دیتا فریم
print(df.index)