import pandas as pd

data1 = {'NAME': ['TaeYeon', 'Jenny', 'YuJu'],
         'GROUP': ['SNSD', 'BlankPink', 'GFriend'],
         'BORN': ['1989-03-09', '1996-01-16', '1997-10-04'],
         'AGE': [33, 26, 25],
         'COMPANY': ['SM', 'YG', 'Source_Music'],
         'TEST1': ['t1', 't2', 't3']
         }

df1 = pd.DataFrame(data1)
print(df1['AGE'], end='\n\n')

data2 = {'NAME': ['태연', 'Jenny', 'YuJu'],
         'GROUP': ['SNSD', 'BlankPink', 'GFriend'],
         'BORN': ['1989-03-09', '1996-01-16', '1997-10-04'],
         'AGE': [33, 26, 25],
         'COMPANY': ['SM', 'YG', 'Source_Music'],
         'TEST2': ['t1', 't2', 't3']
         }
df2 = pd.DataFrame(data2)
print(df2['AGE'], end='\n\n')

# 같은 element는 병합된다.
merge_age = pd.merge(df1['AGE'], df2['AGE'])
print(merge_age, end='\n\n')
merge_group = pd.merge(df1['GROUP'], df2['GROUP'])
print(merge_group, end='\n\n')

# 공통된 값들만 출력, -> 제니, 유주
merge_name = pd.merge(df1['NAME'], df2['NAME'])
print(merge_name, end='\n\n')

# 1가지라도 다른 원소가 있으면 그 row는 출력 안됨
merge_total = pd.merge(df1, df2)
print(merge_total)

