import pandas as pd


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)