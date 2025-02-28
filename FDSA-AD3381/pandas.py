# import pandas as pd
# df=pd.read_csv(" D: \covid.csv”)
# print(df)
# df.set_index("location",inplace=True)
# print(df)
# y=df['total_cases']
# print(y)
# y=df[["date","total_cases"]]
# print(y)
# x=df.loc['India']
# x.tail(5)
# x=df.loc[["Aruba 01","Afghanistan 02"]]
# x.head(5)
# z=df.loc[["Aruba","India"],["date","total_cases_per_million"]]
# print(z)
# R=df.loc[:,["total_cases","total_deaths"]]
# print(R)
# data=pd.read_csv("D:/owid-covid-data1.csv")
# d=data.drop(["iso_code"],axis=1)
# print(d)
# df=pd.read_csv("D:/owid-covid-data1.csv")
# data=df.rename(columns={"location":"place","date":"year","total _cases ":"cases"})
# print(data)