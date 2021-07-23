# fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# print(fruits)
#
# b = {'aaaa', 'bbbb', 'cccc', 'bbbb'}
# d = {'aaaa'}
# e = set('aaaa')
# print(type(b))
# print("d>>", d)
# a = set('apply')
# print("b>> ", b)

# union 합집합, intersection 교집합, difference 차집합(앞에 변수가 주체)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
# c = a | b

# 합집합
c = set.union(a, b)
print("union >> ", c, end='\n\n')

# 교집합
d = set.intersection(a, b)
print("intersection >> ", d, end='\n\n')

# 차집합
e = set.difference(a, b)
f = set.difference(b, a)
print("difference a-b >> ",  e)
print("difference b-a >> ", f, end='\n\n')

# 대칭 차집합(중복값은 제외)
h = set.symmetric_difference(a, b)
print("대칭 차잡합 >> ", h, end='\n\n')

# 업데이트
# a.update(5)  # set이라서 정수 안됨, set을 만들어줘야함
a.update({5})
a.update([5])

print("업데이트 a >> ", a, end='\n\n')

# 대칭 업데이트 (겹치지 않는 요소만 저장)
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print("a >>", a)

a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})
print("symethic 겹치지 않는 요소 등록  >> ", a, end='\n\n')


