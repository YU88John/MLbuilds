import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.head())
#sns.jointplot(x='fare', y='age', data=titanic, kind='scatter',xlim=[-100,600],ylim=[0,80])
#sns.displot(titanic['fare'],bins=30)
#sns.boxplot(data=titanic, x='class',y='age',palette='rainbow')
#sns.swarmplot(data=titanic,x='class',y='age',palette='flare')
#sns.countplot(data=titanic,x='sex')
#sns.heatmap(titanic.corr(),cmap='coolwarm',vmax=0.8)
#plt.title('titanic.corr()')
arg = sns.FacetGrid(data=titanic,col='sex',ylim=(20,120),xlim=(0,80))  #like matplotlib supblot
arg.map(sns.histplot,'age')
plt.show()