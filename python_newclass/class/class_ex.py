class Counter:

    def __init__(self, value = 0):
        self.value = value

    def increment(self, delta = 1):
        self.value += delta

    def decrement(self, delta = 3):
        self.value -= delta

# 인스턴트 메서드 활용
cc = Counter()
cc.value
print(cc.value)

cc.increment(3)
print(cc.value)

cc.decrement(2)
print(cc.value)
print()

dd = Counter()
dd.value = 40
print(dd.value)
