# def ten_div(x):
#     x = int(input("숫자 입력: "))
#     return 10 / x
#
#
# # print(ten_div(2))
# # print(ten_div(0))  # error  ZeroDivisionError: division by zero
#
# try:
#     x = int(input("숫자 입력: "))
#     y = 10 / x
#     print(y)
# except:
#     print("예외가 발생")
#
# try:
#     print(ten_div(x))
# except:
#     print("예외가 발생했습니다.")

# try, except, else, finally
# y = [10, 20, 30]

# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요:').split())
#     print(y[index] / x)
# except ZeroDivisionError:
#     print("숫자를 0으로 나눌 수 없습니다.")
# except IndexError:
#     print("잘못된 인덱스입니다.")
# else:
#     print(y)
# finally:
#     print("코드 실행 끝~~~")

# # raise 예외
# def three_multiple():
#     try:
#         x = int(input("3의 배수를 입력하세요 : "))
#         if x % 3 != 0:
#             raise Exception("3의 배수가 아닙니다.")  # 예외 발생을 인위적으로 함.
#         print("x >> ", x)
#
#     except Exception as e:  # 예외 발생이되어서 잡음.
#         print("예외가 발생했습니다 : ", e)
#
#
# three_multiple()

# 멀티 try, exception
def three_multiple():
    try:
        x = int(input("3의 배수를 입력하세요 : "))
        if x % 3 != 0:
            raise Exception("3의 배수가 아닙니다.")  # 예외 발생을 인위적으로 함.
        print("x >> ", x)

    except Exception as e:  # 예외 발생이되어서 잡음.
        print()
        print("three_ multiple 함수에서 예외가 발생했습니다 : ", e)
        raise  # 위로 한번 더 던져줄때는 raise 멀티 try


try:
    three_multiple()
except Exception as e:
    print("스크립트 파일에서부터 예외가 발생했습니다 : ", e)





