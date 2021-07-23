# 클래스 메서드
class Person:
    count = 0   # 클래스 변수

    def __init__(self): # 생성자 초기화
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))   # cls로 클래스 속성에 접근


# Person.count = 10   # count에 직접 값을 추가해줌,
james = Person()
maria = Person()

Person.print_count()