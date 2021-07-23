# 계좌 입력 정규식 - zfill
class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0  # 입금되어 있는 금액
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "sc은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # zfill -> 빈칸을 0으로 채우는 함수
        num2 = str(num2).zfill(2)  # rjust(width, [fillchar])
        num3 = str(num3).zfill(6)
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    @classmethod
    def get_account_num(cls):  # class 변수 출력 정의
        print(cls.account_count)

    # 입금
    def deposit(self, amount):
        if amount >= 1:  # 1원 이상 입금 가능
            # 기록들을 list에 계속 넣어줌
            self.deposit_log.append(amount)  # 입금 기록 남기기
            self.balance += amount  # 잔액에 amount 입금

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:  # 5번씩마다 이자 지급
                self.balance = (self.balance * 1.01)

    # 출금
    def withdraw(self, amount):
        if self.balance > amount:
            # 기록들을 list에 계속 넣어줌
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        # 담겨져있는 기록들을 출력해야함
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        # 담겨져있는 기록들을 출력해야함
        for amount in self.deposit_log:
            print(amount)


park = Account("박상이", 30000)
kim = Account("김상건", 2000000)
print(kim.name, kim.balance, kim.bank, kim.account_number, "계좌 개설 >> ", Account.account_count)

lee = Account("이지영", 3000000)
print(lee.name, lee.balance, lee.bank, lee.account_number, "계좌 개설 >> ", Account.account_count)
kim.get_account_num()
print()

kim.deposit(50000)  # 입금 완료
print("50000원 입금 >> ", kim.balance, end='\n\n')

kim.display_info()
print()
lee.display_info()

lee.deposit(11000)
lee.deposit(12000)
lee.deposit(13000)
lee.deposit(14000)
lee.deposit(15000)
print()
lee.display_info()

data = []

data.append(kim)
data.append(lee)
data.append(park)

print()
print("100만원 이상")

for c in data:
    if c.balance >= 100000:
        c.display_info()
    print()

# deposit 기록
kim.deposit_history()
print()

# withdraw 기록
lee.withdraw(3000)
lee.withdraw(2000)
lee.withdraw(6000)
lee.withdraw_history()


