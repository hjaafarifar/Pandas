import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# اتریبیوت dtype نوع داده ای هر ستون را مشخص میکند
print(df.dtypes,'\n',100*'*')

# برسی میکند از هر نوع داده ای چند نمونه وجود دارد
print(df.dtypes.value_counts(),'\n',100*'*')

# اطلاعات جامعی راجب دیتا فریم به ما میدهد
print(df.info(),'\n',100*'*')

# هر ستون از دیتا فریم یک دیتا سریز است که میتوانیم با متد ها و اتریبیوت های دیتا فریم به اطلاعات دیتا سریز دسترسی پیدا کنیم
print(df.type.info())
