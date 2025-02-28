import pandas as pd
df1=pd.read_csv("D:/df1.csv")
df1
df2=pd.read_csv("D:\df2.csv")
df2
pd.merge(df1,df2, on= 'customer_id', how="inner")
pd.merge(df1,df2,on='customer_id',how="outer")
pd.merge(df1,df2,on='customer_id',how="left")
pd.merge(df1,df2,on='customer_id',how="right")
