import math
# Point 기본
class Point2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def PointPrint(self):
        print('{} {}'.format(self.__x, self.__y))

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y


p1 = Point2D(x=30, y=20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2
# print('p2: {} {}'.format(p2.x, p2.y))

p1.PointPrint()
p1.setX(40)
p1.PointPrint()

p2.setXY(300, 500)
p2.PointPrint()
# p1.PointPrint()


class LineDraw:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


li = LineDraw(p1, p2)

print()
print("LineDraw ---------------")
li.p1.PointPrint()
li.p2.PointPrint()

a = p2.getX() - p1.getX()
b = p2.getY() - p1.getY()
# c = math.sqrt(a*a + b*b)    # sqrt 함수는 제곱근을 구하는 함수
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))  # 제곱근을 pow 함수로 표현

print()
print("피타고라스 c제곱 >> ", c)
