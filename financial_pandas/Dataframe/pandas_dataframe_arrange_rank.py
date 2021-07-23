from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005760", "ACTS", 1185]
]

columns = ['종목코드', '종목명', '현재가']
df = DataFrame(data=data, columns=columns)
df = df.set_index('종목코드')
print(df, end='\n\n')

df2 = df.sort_values(by='현재가')  # ascending=False이면 역으로 정렬
print(df2, end='\n\n')

df['순위'] = df['현재가'].rank(ascending=False)  # 순위를 먼저 매기고,
df = df.sort_values(by='순위')        # 순위그룹으로 정렬
print(df)




