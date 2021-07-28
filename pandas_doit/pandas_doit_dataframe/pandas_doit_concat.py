import pandas as pd

df1 = pd.read_csv('../pandas_doit_dataframe/data/concat_1.csv')
df2 = pd.read_csv('../pandas_doit_dataframe/data/concat_2.csv')
df3 = pd.read_csv('../pandas_doit_dataframe/data/concat_3.csv')

print('====================기본프레임======================')
print(df1, end='\n\n')
print(df2, end='\n\n')
print(df3, end='\n\n')

# 커럼 이름이 같기때문에 자동 매칭가능
total = pd.concat([df1, df2, df3])
print(total, end='\n\n')

new_Series = pd.Series(['new1', 'new2', 'new3', 'new4'])
print(new_Series, type(new_Series), end='\n\n')

print('====================concat======================')
data = {'A': ['new1'], 'B': ['new2'], 'C': ['new3'], 'D': ['new4']}
df = pd.DataFrame(data)
print("데이터베이스 생성")
print(df, end='\n\n')

# 데이터베이스로 concat가능
df_df = pd.concat([total, df])
print(df_df, end='\n\n')

# 컬럼이 중복되는게 없기에 NaN 출력
df_series = pd.concat([total, new_Series])
print(df_series, end='\n\n')

append_data = total.append(data, ignore_index=True)  # 이전 인덱스를 무시하고, 정수형 인덱스로 변환
print(append_data, end='\n\n')

# axis
print('====================axis======================')
total_row = pd.concat([df1, df2, df3], axis=0)
print(total_row, end='\n\n')

# A, B, C, D -> 0, 1, 2, 3 정수로 변경
total_cols = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
# print(total_cols, end='\n\n')

df1.columns = ['a', 'b', 'c', 'd']
df2.columns = ['e', 'f', 'g', 'h']
df3.columns = ['a', 'c', 'f', 'h']

# 열이 모두가 다 다르더라도 데이터프레임 생성가능
# 하지만 없는 값들은 NaN값 처리
change_total = pd.concat([df1, df2, df3])
print(change_total, end='\n\n')

# join

total_row = pd.concat([df1, df2, df3])
row_df1_df3 = pd.concat([df1, df3], join='inner')
row_df1_df2 = pd.concat([df1, df2], join='inner')
row_df2_df3 = pd.concat([df2, df3], join='inner')
print('====================join======================')
print(total_row, end='\n\n')
print(row_df1_df3, end='\n\n')
print(row_df2_df3, end='\n\n')
print("중복 값이 없는 join - ", row_df1_df2, end='\n\n')