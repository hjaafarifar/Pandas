import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# عملگر های ریاضی (+,-,*,/)
print(df['top_speed']+50,'\n',100*'*')
print(df['top_speed']-100,'\n',100*'*')
print(df['top_speed']*2,'\n',100*'*')
print(df['top_speed']/1.5)