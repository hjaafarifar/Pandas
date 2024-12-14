import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')


# عملگر های ریاضی(< , > , <= ,>=)

# خط زیر با true یا false هر خط را مشخص میکند که شرط برقرار است یا نه
print(df.top_speed<300,'\n',100*'*')

# کد زیر سطر هایی که نهایت سرعتشان از 300 بیشتر باشد را به طور کامل چاپ میکند
print(df[df.top_speed>300],'\n',100*'*')

# logical condition
# برسی میکند که ایا داده های داده شده در دیتا فریم هستند
print(df[df.model.isin(['R8','Phantom'])])
