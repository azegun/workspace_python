class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다(selfmade)')  # Exception 상속 받은 값을 선언

    def checkError(self):
        print("예외 발썡!!!")  # 메서드를 선언해서 NotThreeMultipleError를 발생


def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise NotThreeMultipleError  # 예외 발생 조건 클래스 만듬
        print(x)
    except NotThreeMultipleError as ne:
        # print(ne)  # Exception 상속 받은 값을 선언한값을 받음
        ne.checkError()  # 메서드를 선언해서 NotThreeMultipleError를 선언


three_multiple()