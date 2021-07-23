def calc():
    a = 3
    b = 5

    def mul_add(x):
        print(a, b)
        c = a * x + b
        return c

    return mul_add  # mul_add의 값을 리턴


d = calc()
print(d(10))