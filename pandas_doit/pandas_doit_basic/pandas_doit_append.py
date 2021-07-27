import pandas as pd
import numpy as np

df = pd.read_csv('../pandas_doit_basic/data/scientists.csv')

born = df['Born']
age = df['Age']

convert_date = born.astype(np.datetime64)
df1 = df.append(convert_date)
print(df1, df1.dtypes)


data = {'NAME': ['태연', '제니', '유주'],
        'GROUP': ['소시', '블핑', '걸프'],
        'BORN': ['1989-03-09', '1996-01-16', '1997-10-04'],
        'AGE': [33, 26, 25],
        'COMPANY': ['SM', 'YG', 'S_M']}

df = pd.DataFrame(data=data)
Girls_age = df['AGE']

print(age, end='\n\n')
print(Girls_age, end='\n\n')
print(age + Girls_age)


