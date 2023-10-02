import numpy as np
import pandas as pd

ecom = pd.read_csv("D:\Python\Ecommerce Purchases")
print(ecom.head())
print(len(ecom.axes[0]), len(ecom.axes[1]))

hPch = ecom['Purchase Price'].max()
print('The highest price is' , hPch)
lPch = ecom['Purchase Price'].min()
print('The lowest price is' , lPch)

enCh = ecom['Language'].str.contains('en')
print(enCh.sum())

jtLwyr = ecom[ecom['Job'] == 'Lawyer']
print(jtLwyr.count())

APchk = ecom['AM or PM'].str.contains('AM', case=True, regex=True)
print(APchk.sum())
PMchk = ecom['AM or PM'].str.contains('PM', case=True, regex=True)
print(PMchk.sum())

cmjob = ecom['Job'].value_counts().head(5)  #can't use with unique, 
print(cmjob)

ppLot = ecom[ecom['Lot'].str.contains('90 WT')]['Purchase Price']
print(ppLot)

