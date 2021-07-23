# for
price_list = [32100, 32150, 32000, 32500]
print("1번 방식")
for list in price_list:
    print(list)
print()

# 리스트의 갯수만큼 반복한다.
print("2번 방식")
for i in range(len(price_list)):
    print(price_list[i])
print()

# enumerate 사용시 key, value 나타내줌.
price_list = [32100, 32150, 32000, 32500]
for i, value in enumerate(price_list):
    print(i, value)
print()

# enumerate로 값
price_list = [32100, 32150, 32000, 32500]
for i, value in enumerate(price_list):
    print(3 - i, value)
print()

# len으로 값
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])
print()

# range 범위를 통한 출력
price_list1 = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(90 + 10 * i, price_list1[i])
print()

# 일반적인 나의 생각
my_list = ["가", "나", "다", "라"]
for i in range(0, 3):
    print(my_list[i], my_list[i+1])
print()

# 추천 range를 통한 출력
for i in range(len(my_list) -1):
    print(my_list[i], my_list[i+1])
print()

my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list) -2):
    print(my_list[i], my_list[i+1], my_list[i+2])
print()

# ramge안에 처음 시작 값, 마지막 값, 규칙
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list) -1, 0, -1):
    print(my_list[i], my_list[i-1])
print()

# 리스트 순서대로 값을 빼기
my_list = [100, 200, 400, 800]
for i in range(len(my_list) -1):
    print(my_list[i])
print()

# abs함수 음수를 양수로 변환
for i in range(len(my_list) -1):
    print(abs(my_list[i+1] - my_list[i]))
print()

# 중간 숫자 앞뒤로 구해서 평균구하기
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(1, len(my_list) - 1):
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)
print()

# 범위는 둘 중 하나로 잡고, append로 값을 리스트에 다시 넣어주기.
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])
    print(volatility)
print()

# 2차원 리스트
apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
print(apart, end='\n\n')

stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
print(stock, end='\n\n')

# 딕셔너리로 key 리스트로 value
stock1 = {"시가": [100, 200, 300], "종가": [80, 210, 330]}
print(stock1, end='\n\n')

stock3 = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}
print(stock3, end='\n\n')

apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(j, "호")
print()

# 인덱싱으로 -1하기
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart[::-1]:
    for j in i[::-1]:
        print(j, "호")
print()

# 이중 반복 프린트 위치
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for j in i:
        print(j, "호")
        print("-" * 5)
print()


for i in apart:
    for j in i:
        print(j, "호")
    print("-" * 5)
print()

for i in apart:
    for j in i:
        print(j, "호")
print("-" * 5, end='\n\n')

# 2중 반복문 돌리기
data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

# 0.014 수수료 곱하기
result = []
for i in data:
    for j in i:
        result.append(j * 1.00014)
print("1차 배열로 담기 >> ", result)

# 2차원 배열로 저장하기
result = []
for i in data:
    sub = []   # print 출력해서 어떤 값이 나오는지 확인.
    for j in i:
        sub.append(j * 1.00014)  # print 출력해서 어떤 값이 나오는지 확인 - 마지막값이 최종 출력 값..
    result.append(sub)  # 마지막 출력 값들이 입력되면 배열에 2차배열로 담을 수 있음.
print("2차 배열로 담기 >> ", result, end='\n\n')

ohlc = [
        ["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]
        ]

# []배열 인덱싱 1번부터 부르면됨.
for i in ohlc[1:]:
    print(i[3])
print()

# if 조건문으로 비교
# 출력되는 값의 type을 확인하면서 조건을 건다.
for i in ohlc[1:]:
    if i[3] > 150:
        print(i[3])
print()

for i in ohlc[1:]:
    if i[3] >= i[0]:
        print(i[3])
print()

volatility = []
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    volappend = i[1] - i[2]
    volatility.append(volappend)
print("고가와 저가를 append로 리스트에 넣기 >> ", volatility)

for i in ohlc[1:]:
    if i[3] > i[0]:
        print("리스트 안의 값들끼리 비교해서 두 값의 차 >>", i[1] - i[2])
print()

# 토탈 값을 구할때는 변수 선언해주고 거기에다가 다 넣을 수 있게 만들기
profit = 0
for i in ohlc[1:]:
    profit += i[3] - i[0]
print("토탈 손익금 >> ", profit)