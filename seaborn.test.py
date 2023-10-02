import seaborn as sns
import matplotlib.pyplot as plt  #even with seaborn, we need to add plt.show() for the visualization
tips = sns.load_dataset('tips')
#print(tips.head(5))

#sns.displot(tips['total_bill'], bins=30)
#sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex')
#sns.rugplot(data=tips, x='total_bill',y='tip')
#sns.pairplot(data=tips,hue='sex',palette='coolwarm',diag_kind='hist')
sns.kdeplot(data=tips)  #kde = kernel density estimation = calculated based on normal distribution of the data
#and density
plt.show()