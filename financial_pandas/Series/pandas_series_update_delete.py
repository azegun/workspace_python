from pandas import Series

data_ice = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
ice = Series(data=data_ice, index=index)
print(ice, end='\n\n')

# index를 통한 수정
print("index를 통한 수정")
ice.loc['메로나'] = 1500
print(ice, end='\n\n')

# index를 통한 추가
print("index를 통한 추가")
ice.loc['비비빅'] = 3000
print(ice, end='\n\n')

# index를 통한 추가 (index만 가능)
print("index를 통한 삭제")
print(ice.drop('비비빅'), end='\n\n')

# 인덱스 수정
data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
s.index = 'A'+s.index
print("index추가해서 규칙", end='\n\n')
print(s)

# 엑셀로 추가하기.
s.to_excel("data.xlsx")
