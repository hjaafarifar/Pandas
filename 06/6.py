import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# گرفتن یک قطعه از یک دیتا فریم با استفاده از نام ستون
print(df.loc[5:9,['type','top_speed']],'\n',100*'*')# df.loc[first_index:second_index,[columns name]]

# گرفتن یک قطعه از یک دیتا فریم با استفاده از اندیس
print(df.iloc[12:20,[2,5]])