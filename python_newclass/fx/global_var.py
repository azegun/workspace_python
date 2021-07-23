x = 1


# 같은 x로 선언하기에 A안에 x선언 전에는 값이 없음.
def A():
    x = 20
    print("1 >> ", x, locals(), sep=', ', end='\n\n')

    def B():
        nonlocal x
        print("nonlocal >> ", x)  # x = 20
        x = 30
        print("2 >>", x, end='\n\n')  # x = 30

        def C():
            global x
            print("global >> ", x)
            x = x + 100
            print("3 >> ", x)

        print("C() >> ", x)
        C()

    print("B() >> ", x)  # x = 20
    B()


print("A() >> ", x)  # x = 1
A()  # x = 20