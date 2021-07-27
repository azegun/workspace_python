import pandas as pd

df = pd.read_csv('../pandas_doit_basic/data/scientists.csv')
print(df, df.dtypes, end='\n\n')

# datetime 변경 format= '%Y/%m/%d
born_change = pd.to_datetime(df['Born'], format='%Y/%m/%d')
died_change = pd.to_datetime(df['Died'], format='%Y/%m/%d')
print(born_change, end='\n\n')

print(died_change, end='\n\n')
df['Born'] = born_change
df['Died'] = died_change
print(df, df.dtypes, end='\n\n')

# 삭제는 drop axis= 1 은 열
drop_born = df.drop(['Born', 'Died'], axis=1)
print(drop_born, end='\n\n')

sort = df.sort_values(by='Name', ascending=False)
print(sort)

