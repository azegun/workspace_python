from pandas import Series

data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
print(s, end='\n\n')

# 정렬 (오름차순) - value 기준
s1 = s.sort_values()
print("오름차순")
print(s1, end='\n\n')

# 정렬 (내림차순) - value 기준
s2 = s.sort_values(ascending=False)
print("내림차순")
print(s2, end='\n\n')

print("랭킹별로")
print(s.rank(), end='\n\n') # 1.0 1등, 2.0 2등......

print("랭킹별 반대로")
oposite_rank = s.rank(ascending=False)
print(oposite_rank)



