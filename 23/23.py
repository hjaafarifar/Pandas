import pandas as pd
from pathlib import Path


mypath=Path('../pandas/23')
df=pd.read_csv(mypath/'data2.txt')

# syntax کد
# معمولا برای گروه بندی کردن یک قسمت از دیتا فریم و معدل گرفتن قسمتی از درتا فریم بر اساس نوع داده ها استفاده میشود

# pd.pivot_table(  data=دیتا فریم مورد نظر  ,
#                  index=ستونی که قرار است رو ان گروه بندی انجام شود   ,
#                  values=عملیات میانگین روی کدام داده صورت گیرد ,
#                  columns=بر اساس ستون مورد نظر,
#                  aggfunc=توابع تجمیعی مانند sum , mean ,...,
#                  fill_value=پر کردن nan ها با مقدار دلخواه
#                                                            )


# در کد زیر میانگین فروش هر محصول را محاسبه کرده و نمایش میدهد
first=pd.pivot_table(data=df,index='ProductName',values='QuantitySold')
print(first)

# در کد زیر میانگین فروش هر محصول بر اساس نوع پرداخت و اسم فروشنده برسی میکند
second=pd.pivot_table(data=df,index='PaymentMethod',values='QuantitySold',columns='CustomerName',fill_value=0)
print(second)