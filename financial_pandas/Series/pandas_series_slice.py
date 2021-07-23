from pandas import Series

data_ice = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
ice = Series(data=data_ice, index=index)
print(ice, end='\n\n')

#  파이썬 리스트와 달리 연속적이지 않은 값들에 대해서도 슬라이싱 할 수 있습니다.
# 행에 대한 슬라이싱은 2까지
print("인덱스 [0:2] ")
print(ice.iloc[0:2], end='\n\n')

# 인덱스 슬라이싱은  2-1을 가져오는데 행까지
print("행 [메로나:하겐다즈]")
print(ice.loc['메로나':'하겐다즈'])