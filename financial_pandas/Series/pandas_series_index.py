from pandas import Series

# 시리즈 객체를 생성하려면 데이터를 파이썬 리스트로 표현한 후 리스트 객체를 생성자의 인자로 넘겨주면 됩니다
# 시리즈는 인덱스 자동 할당
data = [1, 2, 3]
s = Series(data)
print(s)
print(s * 10, end='\n\n')

data_ice = [1000, 2000, 3000]
index = ['메로나', '구구콘', '하겐다즈']   # 인덱스를 설정해주면 기본 정수값을 대체

s = Series(data=data_ice, index=index)
print(s, end='\n\n')

# 시리즈 객체에 대해 인덱싱 및 슬라이싱 할 때 행 번호와 인덱스를 둘 다 사용할 수 있습니다.

index = ['2019.05.31', '2019.05.30', '2019.05.29', '2019.05.28', '2019.05.27']
data_close = [42500, 42550, 41800, 42550, 42650]

close = Series(data=data_close, index=index)
print(close, end='\n\n')
print("Series.index()", close.index, end='\n')
print("Series.values()", close.values, end='\n\n')

# 시리즈 객체 대한 인덱싱은 iloc 속성, loc 속성, 또는 대괄호([ ]) 기호를 사용합니다.

# 행 번호를 사용해서 인덱싱할 때 iloc 속성을 사용
# 인덱스를 사용할 때 loc 속성을 사용

data = [1000, 2000, 3000]
s = Series(data=data)
print("iloc 인덱싱")
print(s)
print("iloc[0] > ", s.iloc[0])
print("iloc[1] > ", s.iloc[1])
print("iloc[2] > ", s.iloc[2])
print("iloc[-1] > ", s.iloc[-1], end='\n\n')   # -를 하면 역방향


print("loc 인덱싱")
print("loc[0] > ", s.loc[0])
print("loc[1] > ", s.loc[1])
print("loc[2] > ", s.loc[2])
# loc는 인덱스를 통해서 출력하므로, 인덱스가 없는 부분은 에러 발생
# print("loc[-1] > ", s.loc[-1], end='\n\n')

print()
data_ice = [1000, 2000, 3000]
index = ['메로나', '구구콘', '하겐다즈']   # 인덱스를 설정해주면 기본 정수값을 대체
ice = Series(data=data_ice, index=index)

print(ice.iloc[0])
print(ice.loc['메로나']) # loc는 인덱스로 출력




