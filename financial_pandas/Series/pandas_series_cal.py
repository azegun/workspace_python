from pandas import Series

mine = Series([10, 20, 30], index=['NAVER', 'SKT', 'KT'])
wife = Series([20, 30, 40], index=['SKT', 'NAVER', 'KT'])

total = mine + wife
print("mine + wife Series")
print(total, end='\n\n')

data = Series([10, 20, 30], index=['NAVER', 'SKT', 'KT'])
data2 = data * 10
print(data2, end='\n\n')

# 만약 인덱스를 지정하지 안ㄶ을 시 정수 인덱스가 맵핑됨

high = Series([42800, 42700, 42100, 42950, 43000])
low = Series([42150, 42150, 41300, 42150, 42350])

diff = high - low
print(diff, end='\n\n')
print("변동폭이 가장 큰 값", diff.max())
