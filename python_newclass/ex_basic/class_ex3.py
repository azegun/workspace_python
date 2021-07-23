
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def information(self):
        print("바퀴수 ", self.wheel)
        print("가격 ", self.price)


car = Car(4, 4000)
print("바퀴:", car.wheel, "가격:", car.price)


class Bike(Car):
    def __init__(self, wheel, price, machine):
        super().__init__(wheel, price)  # 상속 하였으니, super로 받으면됨
        # self.wheel = wheel
        # self.price = price
        self.machine = machine

    def information(self):
        super().information()
        print("machine >", self.machine)


class selfCar(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    def information(self):
        super().information()
        print("바퀴수", self.wheel)
        print("가격", self.price)


bicycle = Bike(2, 200, "사미노")
print("자전거 바퀴:", bicycle.wheel, "자전거 가격:", bicycle.price)
print(bicycle.machine, end='\n\n')
bicycle.information()

print()
car = selfCar(4, 100)
car.information()
print()


class parents:
    def __init__(self):
        print("부모생성자")

    def call(self):
        print("parent call")


class child(parents):
    def __init__(self):
        print("자식생성자")
        super().__init__() # 상속 받은거 출력

    def call(self):
        print("child call")
        

Me = child()
Me.call()

