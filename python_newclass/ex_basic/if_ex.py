#뒷자리만 받기
# time = input("현재시간:")
# if time[-2:] == "00":   # 00을 문자열로 받기때문에
#     print("정각 입니다.")
# else:
#     print("정각이 아님")

# contains는 in으로 해결.
# question = input("좋아하는 과일은?")
# fruit = ["사과", "포도", "홍시"]
# if question in fruit:
#     print("정답입니다.")
# else:
#     print("땡!")
#     question = input("좋아하는 과일은?")


# season = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# user = input("제가 좋아하는 계절은?")
# if user in season:
#     print("좋아함")
# else:
#     print("아님")
#     user = input("제가 좋아하는 계절은?")
# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# user = input("좋아하는 과일은?")
# if user in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답.")
#     user = input("좋아하는 과일은?")

# 환율 변환기
# 환율 = {"달러": 1167,
#         "엔": 1.096,
#         "유로": 1268,
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split(" ")
# print(float(num) * 환율[currency], "원")

# 숫자 비교
# num1 = input("input number1: ")
# num2 = input("input number2: ")
# num3 = input("input number3: ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
#
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)
#

# 앞 전화번호로 확인하는 유효성
# number = input("휴대전화 번호 입력")
# num = number[0:3]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")

# 주소 번호로 지역 분리
# addnum = input("우편번호 : ")
# addnum = addnum[:3]
# if addnum in ["010", "011", "012"]:
#     print("강북구")
# elif addnum in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")

# 주민번호 스플릿으로 자르고, 앞번호로 확인

# idennum = input("주민등록번호 :")
# idennum = idennum.split("-")[1]
# if idennum[0] == "1" or idennum[0] == "3":
#     print("남자")
# else:
#     print("여자")

# 주민번호 스플릿으로 자르고 뒷자리로 지역 판별
# idennum = input("주민등록번호 :")
# backnum = idennum.split("-")[1]
# print("backnum >> ", int(backnum[1:3]))
# if 0 <= int(backnum[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

# 주민번호 유효성 판단

num = input("주민등록번호: ")
cal1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
cal2 = 11 - (cal1 % 11)
cal3 = str(cal2)
print("num[-1]>> ", num[-1], "cal3[-1] >> ", cal3[-1])
if num[-1] == cal3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#
# print(btc)
#
# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])
#
# if (시가 + 변동폭) > 최고가:
#     print("상승장")
# else:
#     print("하락장")
