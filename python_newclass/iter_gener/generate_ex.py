def number_generator():
    yield 0
    yield 1
    yield 2


print(number_generator().__next__())
print(number_generator().__next__())
print(number_generator().__next__())

for i in number_generator():
    print(i)
print()


def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


for i in number_generator(3):
    print(i)

