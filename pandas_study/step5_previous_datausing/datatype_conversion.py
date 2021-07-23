import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
              'weight', 'acceleration', 'model year', 'origin', 'name']

print("# 각 열읮 자료형 확인")
print(df.dtypes, '\n')

print("# horsepower 열의 고유값 확인")
print(df['horsepower'].unique(), '\n')

nam_list = [int(i) for i, a in df['horsepower'].items() if a == "?"]
print("'?' 데이터 검색 결과 : ", [(i, val) for i, val in df['horsepower'].items() if i in nam_list], end='\n\n')

print("# 누락 데이터('?') np.nan으로 변경")
df['horsepower'].replace('?', np.nan, inplace=True)  # '?'을 np.nan으로 변경

nan_list = [int(i) for i, a in df['horsepower'].isna().items() if a is True]
print("'nan' 데이터 검색 결과 : ", [(i, val) for i, val in df['horsepower'].items() if i in nan_list], end='\n\n')

df.dropna(subset=['horsepower'], axis=0, inplace=True) # 누락데이터 행을 삭제
nan_list = [int(i) for i, a in df['horsepower'].isna().items() if a is True]
print("'nan' 데이터 검색 결과 : ", [(i, val) for i, val in df['horsepower'].items() if i in nan_list], end='\n\n')
