import numpy as np
import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
#print(df)

#1
print(df[df['Liczba']>1000])
#2
print(df[df['Imie']=='JAKUB'])
#3
grouped3 = df.groupby(['Rok'])
print(grouped3.count())
#4
grouped4 = (df[df['Rok']<2006])
print(grouped4.groupby(['Rok']).sum())
#5---
grouped5 = (df[df['Rok']<2018])
print(grouped5.groupby(['Plec']).sum())
#6---
grouped6 = (df[df['Rok']<2018])
print(grouped6.groupby('Plec').max())
#7---
