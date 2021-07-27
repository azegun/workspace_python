import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('../pandas_doit_basic/data/Football.csv')
df.to_excel('../pandas_doit_basic/save/Football.xlsx')

df_read = pd.read_excel('../pandas_doit_basic/save/Football.xlsx')
print(type(df_read), df.info(), end='\n\n')
print("======골======")
goal = df_read[['Team', 'Goals']]
print(goal.max(), end='\n\n')
df_read = df_read.set_index('Team')
print(df_read, end='\n\n')

max_goal = df_read['Goals'].max()
print("최고골", max_goal, end='\n\n')
barsha = df_read.loc['Barcelona']
m_u = df_read.loc['Manchester United']
print(barsha, m_u)

