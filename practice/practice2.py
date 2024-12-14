import pandas as pd
from pathlib import Path

mypath=Path('../pandas/practice')
df=pd.read_csv(mypath/'data2.txt')

# با گرفتن اطلاعات هر ستون از دیتا فریم میفهمیم Data ما از نوع object است برای تبدیل ان به date time به صورت زیر عمل میکنیم
print(df.info())

x=df['Date']
df['Date']=pd.to_datetime(x)

print(df.info())