class Person:
    def __init__(self, name, age, address):
        self.hello = "안녕하세요."
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

    def getAge(self):
        print('나는 {0}이고, 나이는 {1}입니다.'.format(self.name, self.age))


maria = Person('마리아', 20, '서울시 서초구 강호동')
maria.greeting()
maria.getAge()
maria.age = 50  #새로 정의
maria.getAge()

print("이름 >> ", maria.name)
print("나이 >> ", maria.age)
print("주소 >> ", maria.address)

