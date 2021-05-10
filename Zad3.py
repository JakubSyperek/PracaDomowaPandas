import pandas as pd
import xlrd
import openpyxl

df = pd.read_csv('zamowienia.csv', header=0, sep=";",decimal=',')
#print(df)

#1
print(df["Sprzedawca"].unique())

#2---
#print(df['Utarg'].max())

#3---
#print(df.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']}))

#4---
#print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))