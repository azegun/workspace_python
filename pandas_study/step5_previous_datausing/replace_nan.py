import seaborn as sns

df = sns.load_dataset('titanic')
print("# age 열의 첫 10개 데이터 출력 (5행에 NaN 값")
print(df['age'].head(10), '\n')

print("# age 열의 NaN값을 다른 나이 데이터의 평균으로 변경하기")
mean_age = df['age'].mean(axis=0)
print("mean_age", mean_age, end='\n\n')

df['age'].fillna(mean_age, inplace=True)

print("# age 열의 첫 10개 데이터 출력 (5 행에 NaN 값이 평균으로 대체)")
print(df['age'].head(10))

print("# embark_town 열의 829행의 NaN 데이터 출력")
print(df['embark_town'][825:830], '\n')

print("# embark_town 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기")
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq, '\n')

df['embark_town'].fillna(most_freq, inplace=True)

print("# embark_town 열 829행의 NaN 데이터 출력(NaN 값이 most_freq값으로 대체)")
print(df['embark_town'][825:830])

print("# embark_town 열의 829행의 NaN 데이터 출력")
print(df['embark_town'][825:830])
print()

print("# embark_town 열의 NaN값을 바로 앞에 있는 828행의 값으로 변경하기")
df['embark_town'].fillna(method='ffill', inplace=True)
print(df['embark_town'][825:830])