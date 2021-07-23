import pandas as pd
from pandas import DataFrame

data = [
    [9450, 9490, 9160, 9220, 145794],
    [9380, 9570, 9330, 9490, 57571],
    [9220, 9400, 9100, 9380, 131427],
    [9200, 9250, 9030, 9230, 66893],
    [9350, 9600, 9070, 9200, 138861]
]

columns = ['시가', '고가', '저가', '종가', '거래량']
date = ["2019-06-07", "2019-06-05", "2019-06-04", "2019-06-03", "2019-05-31"]
df = DataFrame(data=data, index=date, columns=columns)
print(df, end='\n\n')

# dtype='object' 날짜 비교 연산이 어려움
print(df.index)
convert = pd.to_datetime(date)
print(convert, end='\n\n')

print("datetime64로 변경 후 다시 DataFrame")
df1 = DataFrame(data=data, index=convert, columns=columns)
print(df1, end='\n\n')
print(df1.index, end='\n\n')

# 날짜의 구분자가 '-'가 아니라면 datatime64 데이터 타입으로 변환되지 않으므로 format으로 변경해주기

dates = ["19/06/07", "19/06/05", "19/06/04", "19/06/03", "19/05/31"]
convert_dates = pd.to_datetime(dates, format="%y/%m/%d")
print(convert_dates, end='\n\n')

df_date_format = DataFrame(data=data, index=convert_dates, columns=columns)
print(df_date_format, end='\n\n')
print(df_date_format.index, end='\n\n')

# datetime64 변경하면 아래처럼 데이트 검색에 용이하다.
print("----------기간별 검색-----------")
print(df_date_format.loc['2019-05'])



