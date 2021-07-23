import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95,100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print('df', df, sep='\n', end='\n\n')

df2 = df[:]
sub_df2 = df2.drop('수학', axis=1)
print("sub_df2", sub_df2, sep='\n', end='\n\n')

df3 = df[:]
sub_df3 = df3.drop(['영어', '음악'], axis=1)
print("sub_df3", sub_df3, sep='\n', end='\n\n')

df.drop('수학', axis=1, inplace=True)
print("df", df, sep='\n', end='\n\n')

df.drop(['영어', '음악'], axis=1, inplace=True)
print("df", df, sep='\n')