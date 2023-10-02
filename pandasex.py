import pandas as pd
import numpy as np
sal = pd.read_csv('Salaries.csv.zip')
#print(sal.head(10)['BasePay'].mean())  #head=top n rows, to locate a row.. we have to use .loc[] or .iloc[]... 
#for column, we have to use df['column name']
#print(sal.head(10)['OvertimePay'].max())
findingJo = sal.loc[sal['EmployeeName'] == 'JOSEPH DRISCOLL']  #finding the location  sal.loc[] = row-level
#print(findingJo['JobTitle']) #value found[column we want to know]
#print(findingJo['TotalPayBenefits'])

#hPaid = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'] #create a dataframe of the only true(max) value
#then find the specific column value of the true dataframe
#print(hPaid)
#LPaid = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']
#print(LPaid)

avgPy1 = sal[sal['Year'] == 2011 ]['BasePay'].mean()
print(avgPy1)
avgPy2 = sal[sal['Year'] == 2012 ]['BasePay'].mean()
print(avgPy2)
avgPy3 = sal[sal['Year'] == 2013 ]['BasePay'].mean()
print(avgPy3)
avgPy4 = sal[sal['Year'] == 2014 ].head(200)['BasePay'].mean()
print(avgPy4)

unq = sal['JobTitle'].nunique()  #unique = finding values, nunique = counting
print(unq)

topJ = sal['JobTitle'].value_counts().head(5)
print(topJ)

jobone = sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1
print('The specific jobs in 2013 were' , jobone.sum()) #to count only true values, use sum()

ChFdr = np.count_nonzero(sal['JobTitle'].str.contains('Chief', case=True, regex=True)) #to count only true values
print('The job titles with Chief in it are', ChFdr)

sal['lofJT'] = sal['JobTitle'].str.len()
fnl = sal[['TotalPayBenefits','lofJT']].corr()
print(fnl)
