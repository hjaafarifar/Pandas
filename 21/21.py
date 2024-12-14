import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

df.drop_duplicates(inplace=True)

print(df)

x=df['top_speed'].sort_values()

print(x)

def hispeed(speed):
    if 290<speed<330:
        return 'slow'
    elif 330<=speed<420:
        return 'fast'
    elif 420<=speed<500:
        return 'super fast'
    
df['top_speed']=df['top_speed'].map(hispeed)

print(df['top_speed'])

#  در برنامه فوق تابعی نوشته ایم که به سرعت سرعت هر اتومبیل کلمه ای به ان اختصاص میدهد که با استفاده از تابع map ین کار را انجام داده ایم