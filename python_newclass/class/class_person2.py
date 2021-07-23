class Person:
    bag = [] # 클래스 변수, 공유해서 쓰는 값
    bag_class = []

    def __init__(self, name):
        self.name = name  # 인스턴스 변수, 혼자 사용하는 값

    def put_bag(self, stuff):
        self.bag.append(stuff)

    def bag_class(self, stuff):
        Person.bag.append(stuff)


# james = Person("제임쓰~")
# james.put_bag("신의탑")
#
#
# maria = Person("마뤼야~")
# maria.put_bag("윈드브레이커")
#
# print(james.bag)
# print(maria.bag)
#
# print(james.name)
# print(maria.name)

# 클래스로 바로 입력할 수도 있음.

Person.bag.append("백")
print(Person.bag)
print(Person.__dict__)

print()

james = Person("제임스")
print(james.__dict__)
