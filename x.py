import numpy as np
import pandas as pd
import xlrd
import openpyxl

s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'], 'Populacja': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data)
print(df)

print(s[(s>9)])