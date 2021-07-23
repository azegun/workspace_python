# def print_coin():
#     for i in range(100):
#         print("비트코인")
#
#
# print_coin()
# print()
#
#
# def message():
#     print("A")
#     print("B")
#
#
# message()
# print("C")
# message()
#
# print()
# print("A")
#
#
# def message1():
#     print("B")
#
#
# print("C")
# message1()
# print()


def message1():
    print("A")


def message2():
    print("B")


def message3():
    for i in range(3):
        message2()
        print("C")
    message1()


message3()
print()


def fx(x):
    print(x)


fx("ㅇㅇ")
fx(2)
print()


def fx1(a, b):
    print(a + b)


fx1(3, 4)
fx1(7, 8)


def print_with_smile(string):
    print(string + ":D")


print_with_smile("안녕")


def print_upper_price(price):
    print(price * 1.3)


print_upper_price(100)


def print_sum(a, b):
    print(a + b)


print_sum(10, 20)
print()


# 사칙연산 정의
def print_arithmetic_operation(a, b):
    print(a, " + ", b, " = ", a+b)
    print(a, " - ", b, " = ", a-b)
    print(a, " * ", b, " = ", a*b)
    print(a, " / ", b, " = ", a/b)


print_arithmetic_operation(3, 4)
print()


# 조건문 걸어서 최댓값 구하는 정의
def print_max(a, b, c):
    max_num = 0
    if a > max_num:
        max_num = a
    elif b > max_num:
        max_num = b
    elif c > max_num:
        max_num = c


print_max(2, 5, 7)


# 역순으로 값을 구하는 정의
def print_reverse(string):
    print(string[::-1])


print_reverse("pyrhon")
print()


# 평균구하는 함수 정의
def print_score1(a, b, c):
    sum = int(a + b + c)
    avg = sum / 3
    print("평균값 >> ", avg)


print_score1(4, 10, 3)


def print_score2(score_list):
    print("리스트 입력 평균값 >>", sum(score_list)/len(score_list))


print_score2([1, 2, 3])
print()


# 리스트를 반복문으로 돌린 후 if 조건으로 % 몫이 0이면 출력
def print_even(even_list):
    for v in even_list:
        if v % 2 == 0:
            print(v)


print_even([1, 3, 2, 10, 12, 11, 15])
print()


# 딕셔너리 키만 출력하는 정의
def print_keys(dictionary):
    for key in dictionary.keys():
        print(key)


print_keys({"이름": "김말똥", "나이": 30, "성별": 0})
print()


# 딕셔너리 키값으로 벨류값 출력
def print_value_by_key(my_dict, key):
    print(my_dict[key])


my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}

print_value_by_key(my_dict, "10/27")
print()


# 추천 답안
def print_5xn(line):
    chuck_num = int(len(line) / 5)
    for x in range(chuck_num):          # range에 2넣어도됨
        print(line[x * 5: x * 5 + 5])


print_5xn("아이엠어보이유알어걸")
print()


# 규칙 발견해서 규칙으로 정의
def print_5xn1(line):
    for x in range(2):
        print(line[x * 5: x * 5 + 5])


print_5xn1("아이엠어보이유알어걸")
print()


def printmxn(line, num):
    chuck_num = int(len(line) / num)   # chuck_num = 3
    for x in range(chuck_num + 1):
        print(line[x * 3: x * 3 + 3])


printmxn("아이엠어보이유알어걸", 3)
print()


def calc_monthly_salary(annual_salary):
    print(int(annual_salary / 12))


calc_monthly_salary(12000000)
print()


def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)


my_print(a=100, b=200)
print()

def n_plus_1(n):
    return n + 1


n_plus_1(3)     # 출력안됨.
print(n_plus_1(3))


def make_url(url):
    print("www."+url+".com")


make_url("naver")
print()


# 새로운 리스트 선언 후 append로 넣고,  return해주기.
def make_list1(my_list):
    new_list = []
    for i in my_list:
        new_list.append(i)
    return new_list


print(make_list1("abcd"))


# 간단하게 줄여버리기.
def make_list2(my_list):
    return list(my_list)


print(make_list2("abcd"), end='\n\n')


def pickup_even(even):
    even_list = []
    for i in even:
      if i % 2 == 0:
          even_list.append(i)
    return even_list


print(pickup_even([3, 4, 5, 6, 7, 8]), end='\n\n')


# replace로 값 변환
def convert_int(num):
    return int(num.replace(",", ""))


print(convert_int("1,234,567"), end='\n\n')


def cal(num):
    return num + 4


a = cal(10)
b = cal(a)
c = cal(b)
print(c)


def cal1(num):
    return num + 4


def cal2(num):
    num = num + 2
    return cal1(num)


c = cal2(10)
print(c)






