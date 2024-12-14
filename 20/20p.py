import pandas as pd
from pathlib import Path
from random import randint as rnd


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')


def magmoe(searis):
    return searis/5

def minmom(value):
    return value+10

x=df.groupby(['name','model']).agg(taghsim5=('top_speed',magmoe),tafazol=('min_speed',minmom),newtime=('time',lambda x:x.max()+10))
print(x)

# در کد های بالا یک گروه بندی بر اساس نام و مدل انجام شده است و سپس سه ستون با نام های taghsim 5 و tafazol و newtime ایجاد کرده ایم که هر کدام توابعی را روی ستون های اصلی دیتا فریم یعنی
# top_speed , min_speed , time اعمال میکنند