import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df3 = pd.read_csv('df3')

print(df3['a'].plot.hist(xlim=(0.0,1.0),ylim=(0,70),weights=))
plt.show()