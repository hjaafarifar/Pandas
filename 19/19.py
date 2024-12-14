import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# سینتکس gropby     
# dataframe.gropby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, observed=False, dropna=True)


# خط زیر دیتا فریم ا بر اساس نام های شرکت گروه بندی میکند
grouped=df.groupby('name')['top_speed'].sum()
print(grouped,'\n',100*'*')

# خط زیر دیتا فریم را بر اساس نام های شرکت و مدل ماشین گروه بندی میکند
grouped2=df.groupby(['name','model'])['top_speed'].mean()
print(grouped2,'\n',100*'*')

# با استفاده از تابع agg میتوان یک جدول از یک ستون دیتا فریم را به دست اورد که حاصل min max mean sum را محاسبه میکند
grouped3=df.groupby('name').agg({'top_speed':['min','max','mean','sum']})
print(grouped3)