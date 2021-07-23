class calc:

    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

    def sub(self, a, b):
        print(a - b)


# 스태틱매서드는 self가 필요없어서 생성자 선언이 필요없음
# self선언 한 메서드면 생성자 선언해야함.
calc.add(2, 5)
cc = calc()
cc.sub(4, 6)