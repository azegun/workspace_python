from pandas import DataFrame

data = [
    ["037730", "3R", 1510, 7.36],
    ["036360", "3SOFT", 1790, 1.65],
    ["005760", "ACTS", 1185, 1.28]
]

columns = ['종목코드', '종목명', '현재가', '등락율']
df = DataFrame(data=data, columns=columns)
print(df, end='\n\n')
df = df.set_index('종목코드')  # '종목코드'를 인덱스로 지정
print(df['현재가'], end='\n\n')        # DataFrame[]하면 컬럼 출력

# 리스트의 슬라이싱이 연속된 데이터만을 선택할 수 있었던 반면 데이터프레임은 불연속적인 데이터도 쉽게 떼어낼 수 있음

data_slicing = [
    ["037730", "3R", 1510, 7.36],
    ["036360", "3SOFT", 1790, 1.65],
    ["005760", "ACTS", 1185, 1.28]
]

columns = ['종목코드', '종목명', '현재가', '등락율']
df = DataFrame(data=data, columns=columns)
print(df, end='\n\n')

df = df.set_index('종목코드')  # '종목코드'를 인덱스로 지정

select_list = ['현재가', '등락율'] # 슬라이싱 할 컬럼들
print(df[select_list], end='\n\n')

# 컬럼 추가
print()
print("컬럼 추가")

data = [
    [112000, 112500, 109500, 110500],
    [114000, 114500, 110500, 111000],
    [113000, 115000, 112000, 115000],
    [111500, 112500, 110000, 111500],
    [111000, 114000, 109500, 112000]
]

columns = ['시가', '고가', '저가', '종가']
index = ["2019-06-05", "2019-06-04", "2019-06-03", "2019-05-31", "2019-05-30"]

df = DataFrame(data=data, index=index, columns=columns)
df['변동성'] = df['고가'] - df['저가']     # 컬럼 추가
print(df, end='\n\n')

data = [
    [112000, 112500, 109500, 110500],
    [114000, 114500, 110500, 111000],
    [113000, 115000, 112000, 115000],
    [111500, 112500, 110000, 111500],
    [111000, 114000, 109500, 112000]
]

columns = ['시가', '고가', '저가', '종가']
index = ["2019-06-05", "2019-06-04", "2019-06-03", "2019-05-31", "2019-05-30"]
df = DataFrame(data=data, index=index, columns=columns)

# axis = 1은 컬럼의 레이블을 의미, axis = 0은 인덱스를 의미
print("axis = 1 - 컬럼명")
df2 = df.drop('시가', axis=1)
print(df2, end='\n\n')

# 데이터프레임에서 특정 로우를 삭제하기 위해서는 drop 메서드에 삭제할 로우의 인덱스와 axis를 0으로 넘겨주면 됨
print("axis = 0 - 인덱스")
df2 = df.drop('2019-05-30', axis=0)
print(df2, end='\n\n')

# 데이터프레임에서 로우나 칼럼을 바로 삭제하고자 한다면 inplace 항목에 True 값을 넘겨주면 됩니다.
df.drop('2019-05-30', axis=0, inplace=True)
print(df, end='\n\n')

# 듀개이상 row로 삭제
df.drop(['2019-05-31', '2019-06-03'], axis=0, inplace=True)
print(df)