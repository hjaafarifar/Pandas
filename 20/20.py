import pandas as pd
from pathlib import Path
from random import randint as rnd


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# فرض کنید میخواهیم ستون time را حذف کرده و تاریخ رندمی جایگزین ان کنیم به صورت زیر عمل میکنیم

# ابتدا ستون تایم را حذف میکنیم
df.drop('time',axis=1,inplace=True)
print(df)

# ایجاد تایم ها به دو روش
# mytime=[]
# for i in range(len(df)):
#     x=f'{rnd(2015,2024)}/{rnd(1,12)}/{rnd(1,30)}'
#     mytime.append(x)

time=[f'{rnd(2015,2024)}/{rnd(1,12)}/{rnd(1,30)}' for i in range(len(df))]
print(time,'\n',100*'*')


df['datatime']=time
print(df,'\n',100*'*')
# اگر نوع  داده ای از زمان ها بگیریم میگوید ابجکت
print(df.datatime.dtype,'\n',100*'*')

# استفاده از متد زیر برای تغیر نوع داده ای از object به dateandtime
df['datatime']=pd.to_datetime(time)
print(df,'\n',100*'*')
# اگر پس از استفاده از متد بالا نوع داده ای از ستون تایم ها بگیریم میگوید از نوع dateandtime است
print(df.datatime.dtype,'\n',100*'*')

# تغیر ستون از اخر به ستون دوم
df.insert(1,'datatime',df.pop('datatime'))
print(df)