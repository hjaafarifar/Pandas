import pandas as pd
from pathlib import Path


mypath=Path('../pandas')
df=pd.read_csv(mypath/'data.txt')

# افرودن یک سطر به دیتا فریم
# در قطعه کد زیر یک سطر به دیتا فریم اضافه کردم فراموش نشود که برای اضافه کردن یک سطر حتما باید به تعداد ستون ها داده وارد کنیم
df.loc[len(df)]=['Saipa','pride',3090,1000,1,'superlux']
print(df)


# روش دوم 
new=pd.DataFrame({'name':['irankhodro'],'model':['Dena+'],'time':[2030],'top_speed':[200],'min_speed':[0],'type':['sedan']})
df=pd.concat([df,new],ignore_index=True)
print(df)