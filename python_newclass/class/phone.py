class Phone:
    phone_name = '피쳐폰'

    def __init__(self, my_number, my_name):
        print("Phone 생성자 호출")
        self.my_number = my_number
        self.my_name = my_name

    def call(self, number):
        print(f'phone 전화걸기 : {number}')

    def send_msg(self, number, msg):
        print(f'Phone 메시지 보내기 : {number}, {msg}')

    def get_info(self):
        print(f'Phone 내 번호 : {self.my_number}')
        print(f'Phone 내 이름 : {self.my_name}')


# 자식 클래스 : 애플
class ApplePhone(Phone):
    def __init__(self, my_number, my_name):
        super(ApplePhone, self).__init__(my_number, my_name) # 부모
        # print("ApplePhone 생성자 호출 ")

    def button_home(self):
        print("ApplePhone 홈 버튼 눌림")


# 자식 클래스 : 갤럭시
class GalaxyPhone(Phone):
    def __init__(self, my_number, my_name):
        super(GalaxyPhone, self).__init__(my_number, my_name) # 부모
        # print("GalaxyPhone 생성자 호출")

    def button_cancel(self):
        print("GalaxyPhone 취소(뒤로가기) 버튼이 눌렀습니다.")


# 클래스 생성
print("\n1. 각 클래스의 객체 생성")
# phone = Phone("010-2222-2222", "폰은정")
apple = ApplePhone("010-1234-1234", "갑돌")
galaxy = GalaxyPhone("010-3333-2222", "고고")

# 부모 클래스로부터 물려받은 메서드
print("\n2. 부모 클래스의 메서드 호출")
# phone.get_info()
apple.get_info()
galaxy.get_info()

# 본인 메서드
print("\n3. 자식 클래스의 메서드 호출")
apple.button_home()
galaxy.button_cancel()
