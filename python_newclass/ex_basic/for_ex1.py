# for
from builtins import len

list = [100, 200, 300]
for i in list:
    print(i + 10)
print()

list1 = ["김밥", "라면", "튀김"]
for i1 in list1:
    print("오늘의 메뉴 : ", i1)
print()

# 길이 찍어보기
list2 = ["SK하이닉스", "삼성전자", "LG전자"]
for i2 in list2:
    print("리스트안에 인수는 길이 1 >> ", i2, len(i2))
print()

list3 = ['dog', 'cat', 'parrot']
for i3 in list3:
    print("리스트안에 인수는 길이 2 >> ", i3, len(i3), "첫 글자만 출력 >> ", i3[:1])
print()

list4 = [1, 2, 3]
for i4 in list4:
    print("3단 곱하기", "3 x", i4, " = ", 3*i4)
print()

# list for문 돌릴 떄 슬라이싱해주기
list5 = ["가", "나", "다", "라"]
for i5 in list5[::2]:
    print("인덱스로 출력 >> ", i5)
print()

for i5 in list5[::-1]:
    print("리스트 거꾸로 출력 >> ", i5)
print()

# if 조건문으로 출력 나누기
list6 = [3, -20, -3, 44]
for i6 in list6:
    if i6 < 0:
        print(i6)
print()

# 배수를 통한 if
list7 = [13, 21, 12, 14, 30, 18]
for i7 in list7:
    if i7 < 21 and i7 % 3 == 0:
        print(i7)
print()

# 길이를 통한 if
list8 = ["I", "study", "python", "language", "!"]
for i8 in list8:
    if len(i8) > 2:
        print(i8)
print()

# is를 통한 if
list9 = ["A", "b", "c", "D"]
for i9 in list9:
    if i9.isupper():
        print(i9)
print()

for i9 in list9:
    if i9.islower():
        print(i9)
print()

# 첫글자만 대문자로 만들기
print("첫글자 대문자로 바꾸기 1. capitalize()")
for i3 in list3:
    print(i3.capitalize())
print()
print("첫글자 대문자로 바꾸기 2. 슬라이싱")
for i3 in list3:
    first = i3[0]   # 첫글자만 받기
    upp = first.upper()  # 첫글자 대문자로 바꾸고
    print(upp + i3[1:])  # 대문자 바꾼걸 합친다
print()

# 스플릿으로 리스트로 나눠서 출력
list10 = ['hello.py', 'ex01.py', 'intro.hwp']
for i10 in list10:
    list10_split = i10.split(".")
    print(list10_split[0])
print()

list11 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i11 in list11:
    list11_split = i11.split(".")
    if list11_split[1] == "h":
        print(i11)

print()
for i11 in list11:
    list11_split = i11.split(".")
    if list11_split[1] == "h" or list11_split[1] == "c":
        print(i11)
print()

# range를 이용한 리스트
for i in range(100):
    print(i)
print()

for i in range(2002, 2051, 4):
    print(i)
print()

for i in range(1, 31):
    if i % 3 == 0:
        print(i)
print()

# 소수자리 출력
for i in range(10):
    print(i/10)
print()

# 곱하기 출력
for i in range(1, 10):
    print("3 x", i, "=", 3 * i)
print()

for i in range(1, 10, 2):
    print("3 x", i, "=", 3 * i)
print()

# 총 금액 더하기
num = 0
for i in range(1, 11):
    num += i
print(num)
print()

even = 0
for i in range(1, 11, 2):
    even += i
print("홀수의 합 >> ", even)
print()

mul = 1
for i in range(1, 11):
    mul *= i
print("곱하기 >> ", mul)











