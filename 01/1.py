# فراخوانی ماژول pandas
import pandas as pd    


# ایجاد یک dataframe
data=[['BMW',280,'450000$'],['BENZ',250,'500000$'],['Pride',150,'2000000$']]
column=['name','speed','price']
df=pd.DataFrame(data,columns=column,index=[1,2,3])
print(df)

# روش دوم 
df2=pd.DataFrame({'name':['BMW','BENZ','Peride'],'speed':[280,250,150],'price':['450000$','500000$','2000000$']},index=[1,2,3])
print(df2)