from pandas import DataFrame
from pandas import Series

#  로우 단위로 인덱싱하려면 iloc 혹은 loc 속성을 사용

data = [
    ["037730", "3R", 1510, 7.36],
    ["036360", "3SOFT", 1790, 1.65],
    ["005760", "ACTS", 1185, 1.28]
]

columns = ['종목코드', '종목명', '현재가', '등락율']
df = DataFrame(data=data, columns=columns)
df = df.set_index('종목코드')
print(df, end='\n\n')

# loc : 명칭으로 인덱스 iloc : 인덱스 넘버
# loc로 인덱싱한 로우 데이터는 시리즈
# 칼럼 이름이 시리즈의 인덱스로 사용
convert_series = df.loc['036360']
print("DataFrame 에서 Series로 인뎅싱 type : DataFrame > Series")
print(convert_series, type(convert_series), end='\n\n')

print("Series로 변경된 걸 index하기 type : series > str")
print(convert_series['종목명'], convert_series['현재가'], convert_series['등락율'], end='\n\n')

print("df.iloc[0]")
print(df.iloc[0], end='\n\n')
print("df.iloc[-1] : -1은 거꾸로 출력")
print(df.iloc[-1], end='\n\n')

print("df.loc[['037730', '036360']]")
print(df.loc[['037730', '036360']], end='\n\n')

print("df.iloc[[0, -1]]")
print(df.iloc[[0, -1]], end='\n\n')

print()
print("row 추가")
print('loc(날짜) 추가')
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
print(df, end='\n\n')
# Series로 정수를 입력하면, 값 매칭을 해줘야하기 때문에 columns매치
df.loc['2019-05-29'] = Series([109000, 111000, 108500, 109500], index=columns)
print(df, end='\n\n')

# Series 객체로 추가
print("append로 추가 - Series이용")
ohlc = [100000, 130000, 122100, 321232]
s = Series(data=ohlc, index=columns, name='2019-05-28')
new_df = df.append(s)
print(new_df, end='\n\n')

# 데이터프레임 객체로 추가 
print("append로 추가 - DataFrame이용")
ohlc = [[109000, 111000, 105000, 109550]]
row_df = DataFrame(data=ohlc, index=['2019-05-27'], columns=columns)
new_df = df.append(row_df)
print(new_df, end='\n\n')

ohlc1 = [109000, 111000, 105000, 109550]
row_df1 = DataFrame(data=ohlc1)
print(row_df1, type(row_df1))




