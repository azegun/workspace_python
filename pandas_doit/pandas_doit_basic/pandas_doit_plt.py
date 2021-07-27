import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../pandas_doit_basic/data/gapminder.tsv', sep='\t')

print(df)
year_ifeExp = df.groupby('year')['lifeExp'].mean()
plt.title('test title')
plt.xlabel('year')
plt.ylabel('lifeExp')
plt.plot(year_ifeExp, 'o', markersize=2)
plt.show()
