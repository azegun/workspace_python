from pandas import DataFrame

data = [
    ['037730', '3R', 1510, 7.36],
    ['036360', '3SOFT', 1790, 1.65],
    ['005760', 'ACTS', 1185, 1.28]
]

columns = ['종목코드', '종목명', '현재가', '등락률']
df = DataFrame(data=data, columns=columns)
print(df, end='\n\n')

# 인덱스 변경
df = df.set_index('종목코드')
print("인덱스를 컬럼으로 변경 set_index")
print(df, end='\n\n')

# 인덱스로 지정할 것을 매개변수로 따로 지정해서 생성

data1 = [
    ['3R', 1510, 7.36],
    ['3SOFT', 1790, 1.65],
    ['ACTS', 1185, 1.28]
]

index_code = ['037730', '036360', '005760']
columns = ['종목명', '현재가', '등락률']

df_add_index = DataFrame(index=index_code, data=data1, columns=columns)
print(df_add_index, end='\n\n')
df_add_index.index.name = '종목코드'
print("index.name()")
print(df_add_index, end='\n\n')

