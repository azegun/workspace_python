import seaborn as sns
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

pd.set_option('display.max_columns', len(titanic.columns))
pd.set_option('display.max.colwidth', 15)
pd.set_option('display.width', 1000)

print("# titanic 데이터셋", type(titanic), titanic.head(), sep='\n', end='\n\n')

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
# 모든 행중에서 age, fare 가지고오기
df = titanic.loc[:, ['age', 'fare']]
print(df.head(), type(df), sep='\n', end='\n\n')

print("# 데이터프레임에 숫자 10 더하기")
addiction = df + 10
print(addiction.head(), type(addiction), sep='\n')

titanic = sns.load_dataset('titanic')

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
df = titanic.loc[:, ['age', 'fare']]
print(df.tail(), type(df), sep='\n', end='\n\n')

print("# 데이터프레임에 숫자 10 더하기")
addiction = df + 10
print(addiction.head(), type(addiction), sep='\n', end='\n\n')

print("# 데이터프레임끼리 연산하기 (addiction - df")
subtraction = addiction - df
print(subtraction.tail(), type(subtraction), sep='\n')
