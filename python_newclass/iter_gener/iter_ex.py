import random


class A:
    def __init__(self):
        print("dddd")


it = [1, 2, 3].__iter__()   # list로 출력

print(it.__next__())
print(it.__next__())
print(it.__next__(), end='\n\n')

dict_a = {'a': 'aaaaa', 'b': 'bbbbb'}.__iter__()  # dic로 key값 출력
print(dict_a.__next__())
print(dict_a.__next__(), end='\n\n')

it1 = range(3).__iter__()  # 범위입력해서 next 할 수 있음
print(it1.__next__())
print(it1.__next__())
print(it1.__next__(), end='\n\n')


# range 클래스 내부
class Counter:
    def __init__(self, stop):
        self.current = 0  # 현재 숫자 유지,
        self.stop = stop  # 반복을 끝낼 숫자

    def __iter__(self):
        return self       # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 숫자를 1씩 증가함
            return r
        else:
            raise StopIteration


for i in Counter(3):
    print(i, end=" ")  # end=" " : 0 1 2  가로로 출력 가능
print(end='\n\n')


class MyCollection:
    def __init__(self, size):
        self.size = size
        self.data = list(range(self.size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n


coll = MyCollection(10)
for x in coll:
    print(x)
print()


class Counter1:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, item):
        if item < self.stop:
            return item
        else:
            raise IndexError


for i in Counter1(3):
    print(i)
print()

it_convert = iter([30, 40, 50]) # iter를 리스트처럼 매서드로 만든 후 출력.
print(next(it_convert))
print(next(it_convert))
print(next(it_convert), end='\n\n')

# random함수 구하는 방식 1
it_random = iter(lambda: random.randint(0, 5), 2)   # 2라는 숫자가 나오면 작동이 끝
print(next(it_random))
print(next(it_random))
print(next(it_random))
print(next(it_random))
print(next(it_random))
print()


# 반복문을 통한 출력 2  -
# 편리한 방법
for i in iter(lambda: random.randint(0, 5), 2):
    print(i, end=" ")
print()

# while문을 통한 if 조건문
while True:
    i = random.randint(0, 5)
    if i == 2:
        break
    print(i, end=' ')




