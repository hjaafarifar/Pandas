import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# تغیر نام ستون ها رد پانداز

# تغییر نام تمام ستون ها
df.columns=['A','B','C','D','F','G']
print(df,'\n',100*'*')

# تغییر نام ستون های دلخواه
df.rename(columns={'C':'hello','F':'godbye'},inplace=True)
print(df)



