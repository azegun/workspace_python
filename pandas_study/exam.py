import pandas as pd

# 1번문제

exam_data = {'name': ['test1', 'test2', 'test3'],
             'math': [90, 80, 70],
             'eng': [98, 89, 95],
             'music': [85, 95, 100],
             'kor': [100, 90, 90]
             }

df = pd.DataFrame(exam_data)
print(df)
print()

# 2번 문제
df.set_index('name', inplace=True)
print(df, sep='\n', end='\n\n')


# 3번 문제
sr_test1 = df.loc['test1']
print(sr_test1, sep='\n', end='\n\n')

# 4번 문제
sr_eng = df['eng']
print(sr_eng, sep='\n', end='\n\n')

#5번 문제
add_dict = {'name': 'test4', 'math': None, 'eng': 99, 'music': 99, 'kor': 99}
sr_add = pd.Series(add_dict, name=add_dict['name'])
print(sr_add, sep='\n', end='\n\n')

df = df.reset_index()
df = df.append(sr_add, ignore_index=True)
df.set_index('name', inplace=True)
print(df)


#6번 문제
df.dropna(axis=0, inplace=True)
print(df, end='\n\n')

