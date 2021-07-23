import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]

sr = pd.Series(list_data)

print(sr)

idx = sr.index
val = sr.values

# 값이 없이 인덱스를 출력하면 RangeIndex로 type 출력됨.
print(idx)
print('\n')
print(val)
