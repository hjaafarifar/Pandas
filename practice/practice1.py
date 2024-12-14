import pandas as pd
from pathlib import Path

# در داده زیر میخواهیم فروش هایی که در تهران توسط فروشنده مورد نظر و با دستگاه پوز یا پرداخت موبایلی انجام شده را دسته بندی کنیم و توابعی را روی ان اعمال کنیم

mypath=Path('../pandas/practice')
df=pd.read_csv(mypath/'data2.txt')
# print(df)

# در کد زیر داده ها با فروشنده مورد نظر در تهران را جمع اوری میکنیم
x=df[df['City'].isin(['Tehran']) & df['CustomerName'].isin(['Hossein Alavi'])]
# print(x,'\n',100*'*')



# در کد زیر با توجه به ستون مورد نظر توابع را رو ان اعمال میکنیم
myfile=x.groupby(['PaymentMethod'])['TotalSale'].agg(['sum','mean','max','min'])
print(myfile)