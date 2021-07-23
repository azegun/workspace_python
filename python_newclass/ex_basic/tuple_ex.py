my_variable = ()
print(type(my_variable))

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 튜플은 1개만 변수 입력시 무조건, 입력, 안할 시 int로 타입 변경
# 튜플 원소의 값을 변경할 수 없습니다.
# 튜플은 ()생략해도 자동 인식
my_variable = (1,)
print(my_variable, type(my_variable), end='\n\n')

# 튜플을 리스트로 변경
interest = ('삼성전자', 'LG전자', 'SK Hynix')
list = list(interest)
print("tuple To list >> ", list, type(list))

# 리스트에서 튜플로 변경
tuple = tuple(list)
print("list To tuple >> ", tuple, type(tuple))

# 언패킹
temp = ('apple', 'banana', 'cake')
print("언팩킹 타입 >> ", type(temp))
a, b, c = temp
print(a, b, c)

# range 튜플
b = tuple(range(5, 12))
print(b)

















