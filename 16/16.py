import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# گرفتن ستون هایی با نوع داده ای خواص
# مثلا کد زیر ستون هایی که نوع داده ای انها عدد صحیح است را نمایش میدهد
print(df.select_dtypes(include='int'))


