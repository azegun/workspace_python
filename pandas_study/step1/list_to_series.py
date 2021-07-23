import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
list_index = [1, 2, 3, 4, 5]
sr = pd.Series(list_data, index=list_index)

# 값을 넣어주면 Int64Index로 type으로 입력됨
print(sr)
print(type(sr.index), sr.index, sep='\n', end='\n\n')
print(type(sr.values), sr.values, sep='\n', end='\n\n')
