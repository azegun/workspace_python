# class Person:
#     def __init__(self):
#         self.hello = "안녕....hioii"
#         self.beggii = "으악"
#
#     def greeting(self):
#         print(self.hello)
#
#     def beggi(self):
#         print(self.beggii)
#
#
# james = Person();
# bon = Person();
#
# james.greeting()
# james.beggi()
#
class Person():
    def greeting(self):
        print("안녕하세요.")


class University():
    def manage_credit(self):
        print("학점관리")


class Undergraduate(Person, University):
    def study(self):
        print("공부하기")
        

ug = Undergraduate()
ug.study()
ug.greeting()
