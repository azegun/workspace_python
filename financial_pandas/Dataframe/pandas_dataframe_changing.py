from pandas import DataFrame
import numpy as np

data = [
    ['037730', '3R', 1510],
    ['036360', '3SOFT', 1790],
    ['005760', 'ACTS', 1185],
]

columns = ['종목코드', '종목명', '현재가']
df = DataFrame(data=data, columns=columns)
df = df.set_index('종목코드')

print(df.columns)  # index 객체가 저장
print(df.index, end='\n\n')     # 데이터프레임의 컬럼 이름 저장

df.columns = ['name', 'close']  # 컬렁명 변경
df.index.name = 'code'   # index명 변경 '종목코드'->'code'
print(df, end='\n\n')


# 데이터 타입 변경

data = [
    ["037730", "3R", '1,510'],
    ["036360", "3SOFT", '1,790'],
    ["005760", "ACTS", '1,185'],
]


def remove_coma(x):
    return x.replace(',', '')


columns = ['종목코드', '종목명', '현재가']
df = DataFrame(data=data, columns=columns)

print("데이터 타입 변경")
print(df, df.dtypes, end='\n\n')

df['현재가'] = df['현재가'].apply(remove_coma)  # 정수로 바꾸려면 먼저 문자열들을 제거해야함.
print(df, df.dtypes, end='\n\n')        # df.dtypes - object는 str과 같음

df = df.astype({'현재가': np.int64}) # astype으로 정수값으로 변경
print(df.dtypes)




