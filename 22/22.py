import pandas as pd
from pathlib import Path
from random import randint as rnd

# ذخیره فایل در pandas

mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')


# جدا کردن دو ستون از دیتا فریم 
x=df[['model','top_speed']]

# حذف سطر های تکراری
x.drop_duplicates(inplace=True)

# اضافه کردن 50 واحد به ستون top_speed
x['top_speed']=df['top_speed']+50

# ایجاد زمان برای هر سطر
random_time=[f'2020/{rnd(1,12)}/{rnd(1,30)}' for i in range(len(x))]

# اضافه کردن زمان ها به صورت datatime
x['Date']=pd.to_datetime(random_time)
print(x)

# حال دیتا فریم جدی را که ساخته ایم را در قالب یک فایل ذخیره میکنیم
x.to_csv(mypath/'22/22.csv')