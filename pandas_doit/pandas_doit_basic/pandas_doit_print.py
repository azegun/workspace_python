import pandas as pd

df = pd.read_csv('./pandas_doit_basic/data/gapminder.tsv', sep='\t')
print(df.columns, end='\n\n')
print("------------country----------")
print(df['country'], type(df['country']), end='\n\n')

print("------------year----------")
print(df['year'], end='\n\n')

print("------------pop----------")
print(df['pop'], end='\n\n')

print("------------gdpPercap----------")
print(df['gdpPercap'], end='\n\n')

choice = df[['country', 'pop', 'gdpPercap']]
print(choice, end='\n\n')

print(df.loc[:5], end='\n\n')  # index 문자로 출력
print(df.iloc[:5], end='\n\n')             # index로 출력

# 필요한 columns을 먼저 지정 후 인덱스로 필요 범위 출력
choice1 = df[['year', 'country']]
print(choice1[10:100], end='\n\n')

print("df.iloc[10:100] 출력")
print(df.iloc[10:100], end='\n\n')

life = df['lifeExp']
print("mean >>", life.mean(), end='\n\n')
print("sum >>", life.sum(), end='\n\n')
print("shape >>", life.shape, end='\n\n')

lifeAndPop = df[['lifeExp', 'pop']]
print(lifeAndPop.mean(), end='\n\n')

# groupby를 기준하고, df으로 평균 출력
result = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()

print(result)

