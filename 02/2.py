import pandas as pd

# باز کردن یک فایل در  pandas
df=pd.read_csv('C:/Users/BARCELONA/Desktop/pandas/data.txt')# pandas از داده های زیادی پشتیبانی میکند
print(df)


# دسترسی به یک ستون به صورت زیر است
print(df['model'],'\n',100*'*')

# چون هرکدام از نام ستون ها مانند اتریبیوت رفتار میکنند میتوانیم با دات نوتیشین به اطلاعات ان ستون دسترسی پیدا کنیم
print(df.name,'\n',100*'*')

# برای دسترسی به چند ستون از دیتا فریم به صورت زیر عمل میکنیم
print(df[['min_speed','type']])