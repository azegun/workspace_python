import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df, end='\n\n')

df2 = df[:]
print("df2", df2, sep='\n', end='\n\n')

df3 = df2.drop('우현')
print("df3", df3, sep='\n', end='\n\n')

df4 = df[:]
print("df4", df4, sep='\n', end='\n\n')

# axis 0은 열을 삭제 1은 행 삭제
df5 = df4.drop(['우현', '인아'], axis=0)
print("dft", df5, sep='\n', end='\n\n')

df.drop('인아', inplace=True)
print("df '인아' 행 인덱스 삭제 drop inplace=True", df, sep='\n', end='\n\n')

df.drop(['서준', '우현'], axis=0, inplace=True)
print("df' 서준', '우현' 행 인덱스 삭제 drop inplace=True", df, sep='\n')

