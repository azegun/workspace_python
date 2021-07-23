from builtins import print

x = 10
print(x)  # 10

def foo():
    print(x)  # 10


foo()
print()

x = 20
print(x)   # 20
foo()
print(x, end='\n\n')   # 20

x = 10
def foo():
    global x   # 전역변수 사용 global
    x = 20
    print(x)


foo()
print(x)

def print_hello():
    hello = 'hello, world!'
    def print_message():
        print(hello)
    print_message()


print_hello()

print()
# 지역변수, 글로벌변수
def A():
    x = 10
    y = 100

    def B():
        x = 20
        print("locals() >> ", locals(), end='\n\n')  # {'x': 20, 'y': 100} 로칼스 쓰면 들어와있는 값을 딕셔너리로 보여줌

        def C():
            nonlocal x  # 지역변수 밖에 있는 변수
            nonlocal y  # 지역변수 밖에 있는 변수 y가 밖에없어서 그 위에 것 가져옴.
            x = x + 30
            y = y + 300
            print(x)
            print(y)
            print("locals(C) >> ", locals(), end='\n\n')
        C()
    B()
    print(" >", x)
    print("locals() >> ", locals(), end='\n\n')


A()

