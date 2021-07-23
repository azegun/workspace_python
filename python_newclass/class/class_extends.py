class Person():
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("안녕하세요")


# 포함관꼐 has a
class Student(Person):
    def __init__(self, person):
        self.person = person

    def study(self):
        print("공부합니다.")


class Gun():
    def __init__(self, num):
        self.num = num

    def shooting(self):
        print("권총 발사")


class Policeman(Person):

    def __init__(self, num):
        self.gun = Gun(num)

    def emp(self):
        print("근무합니다.")


person2 = Person("김파리")

po1 = Policeman(6)
po1.greeting()
po1.emp()
po1.gun.num = 10
po1.gun.shooting()
print()

st1 = Student(person2)
st1.greeting()
st1.study()


# 상속관계 is a
# class Student(Person):
#     def study(self):
#         print("공부하기")
#
#
# class Student2(Student):
#     def study_hard(self):
#         print("빡세게 공부하기")


# st = Student()
# st.greeting()
# st.study()
# print()
#
# st2 = Student2()
# st2.greeting()
# st2.study()
# st2.study_hard()