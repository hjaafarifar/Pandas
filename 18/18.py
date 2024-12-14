import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# and , or , not ====> & , | , ~ در پاداز شکل عملگر های منطقی به صورت رو به رو میباشد 

# درقطعه کد زیر برسی میکند که در ستون نام ها اگر داده ما برابر با داده های ذکر شده بود ان را چاپ کند
data1=df[(df.name=='BMW') | (df.name=='Tesla')]
print(data1,'\n',100*'*')


data2=df[(df.top_speed==300) & (df.time==2020) ]
print(data2)