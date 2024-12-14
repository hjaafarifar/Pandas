import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# کد زیر یکی از ستون ها را به عنوان اندیس دیتا فریم قرار میدهد
df.set_index('type',inplace=True)
print(df)

