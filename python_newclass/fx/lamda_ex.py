def plus_ten(x):
    return x + 10


print("plus_ten(1)>> ", plus_ten(1), end='\n\n')

# 람다 사용법 - 1줄 사용에 용이함.
la = lambda x: x + 10
print("lamda basic >> ", la(10), end='\n\n')

# 주소만 나옴
print("lambda x: x + 10>> ", lambda x: x + 10)

# x에다가 20넣는다는 뜻 fx(20)이런 뜻  (20)은 매개변수
print("lambda x: x + 10>> ", (lambda x: x + 10)(20), end='\n\n')


# 다중 메서드 출력
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b


c = calc()
print("다중 메서드 lambda로 출력 >> ", c(1), c(2), c(3), c(4), c(5), end='\n\n')

y = 10
la1 = (lambda x: x + y)(10)
print("la1f(x) >> ", la1, end='\n\n')


# 람다를 인수로 표현하기 by Map
def plus_ten(x):
    return int(x + 10)


a = list(map(plus_ten, [1.2, 2.3, 4.3]))
print("함수를 통한 Map >> ", a)

# 위에 선언을 변경 -> 람다
b = list(map(lambda x: x + 10, [1.2, 2.3, 4.3]))
print("lamda by Map >> ", b, end='\n\n')

# 복잡한 람다식 풀어쓰기 *람다에서 else 빠지면 에러*
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

la = list(map(lambda x: str(x) if x % 3 == 0 else x, c))
print("toMap >>", la, end='\n\n')


def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10


d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("조건 메서드 정의해서 만든 값 >> ", list(map(f, d)), end='\n\n')

# 여러 객체를 넣기

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

print("여러개 객체를 map에 lamda로 넣기 >> ", list(map(lambda x, y: x * y, a, b)), end='\n\n')


# filter 사용
def f(x):
    return x > 5 and x < 10


a = [8, 2, 2, 10, 15, 7, 1, 9, 0, 11]
print("filter >> ", list(filter(f, a)))
print("filter by lamda >> ", list(filter(lambda x: x > 5 and x < 10, a)), end='\n\n')


# reduce
def f(x, y):
    return x + y


a = [1, 2, 3, 4, 5]

from functools import reduce
print("reduce >>", reduce(f, a))