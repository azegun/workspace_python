import random


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):   # 프린트 정의
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))


areum = Human("아름", 25, "여자")
areum.who()

areum.setInfo("상건", 30, "남자")
areum.who()
print()


class Stock:
    def __init__(self, name, code, per, pbr, devided_ratio):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.devided_ratio = devided_ratio

    def set_code(self, code):
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_devided(self, devided_ratio):
        self.devided_ratio = devided_ratio


samsung = Stock(None, None, 15.79, 1.33, 2.83)
samsung.set_code("005930")
samsung.set_name("삼성전자")

print(samsung.name, samsung.code, samsung.devided_ratio, samsung.per)
samsung.set_per(12.75)
print("per>> ", samsung.per, end='\n\n')

hyndai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37)


stock_list = []        # 클래스 객체를 list에 넣기떄문에  print 출력 안됨.
stock_list.append(samsung)
stock_list.append(hyndai)
stock_list.append(lg)

for i in stock_list:
    print(i.name)
print()








