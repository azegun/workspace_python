from abc import *


class Human(metaclass=ABCMeta):
    # 추상 메서드
    @abstractmethod
    def walk(self):
        print("Human walk : 사람은 걸어요")

    # 추상 메서드
    @abstractmethod
    def talk(self):
        pass

    # 일반 메서드
    def sleep(self):
        print("Human sleep : 사람은 자요")


# 자식 클래스 : 어른 클래스
class Adult(Human):
    def walk(self):
        print("Adult walk : 어른은 걷습니다.")


# 자식 클래스 : 아기 클래스
class Baby(Human):
    # 추상 메서드
    def walk(self):
        print("Baby walk : 아기는 기어갑니다.")

    def talk(self):
        print("Baby talk : 아기는 옹알이를 합니다.")


# 객체 생성
# human = Human()  # error
# adult = Adult()    # error
baby = Baby()

# 재정의한 추상 메서드
baby.walk()
baby.talk()

# 부모 클래스 메서드
baby.sleep()
