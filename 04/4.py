import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# دسترسی به n داده اول دیتا فریم
print(df.head(8),'\n',100*'*')


# دسترسی به n داده اخر دیتا فریم
print(df.tail(4))

# دز صورتی که به جای n عدد نگذاریم 5 عدد اول و اخر را نمایش میدهد
