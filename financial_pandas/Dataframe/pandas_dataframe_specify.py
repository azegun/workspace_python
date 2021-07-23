from pandas import DataFrame

data = [
    ["037730", "3R", 1510, 7.36],
    ["036360", "3SOFT", 1790, 1.65],
    ["005760", "ACTS", 1185, 1.28]
]

columns = ['종목코드', '종목명', '현재가', '등락율']
df = DataFrame(data=data, columns=columns)
df = df.set_index('종목코드')
print(df, end='\n\n')

# DataFrame에서 Series로
print(df.iloc[0], end='\n\n')
print(df.loc['036360'], end='\n\n')

# Series로 타입 변경되고 나서는 인덱싱기법 안쓰고 []출력
print("iloc[0]으로 특정값 출력")
print("df.iloc[0].loc['종목명']>>", df.iloc[0].loc['종목명'])
print("df.iloc[0]['종목명']>>", df.iloc[0]['종목명'])
print("df.iloc[0].iloc[1]>>", df.iloc[0].iloc[1])
print("df.iloc[0][1]>>", df.iloc[0][1], end='\n\n')

print("df.loc['037730']으로 특정값 출력")
print("df.loc['037730'].iloc[0]>>", df.loc['037730'].iloc[0])
print("df.loc['037730']['종목명']>>", df.loc['037730']['종목명'])
print("df.loc['037730'].loc['현재가']>>", df.loc['037730'].loc['현재가'])
print("df.loc['037730']['현재가']>>", df.loc['037730']['현재가'], end='\n\n')

print("데이터 프레임에서 바로 접근1")
print("df.loc['037730', '현재가']>>", df.loc['037730', '현재가'])
print("df.iloc[0, 0]>>", df.iloc[0, 0], end='\n\n')

print("데이터 프레임에서 바로 접근2")
print("df['종목명'].loc['037730']>>", df['종목명'].loc['037730'])  # loc는 인덱스(종목코드)로 지정 l = literal이라고 생각
print("df['종목명']['037730']>>", df['종목명']['037730'])             
print("df['현재가'].iloc[2]>>", df['현재가'].iloc[2])                             # i  = index라고 생각
print("df['현재가'][2]>>", df['현재가'][2], end='\n\n')

# 범위를 구할 떄는 [[]]
print("범위로 값을 가져오기 - 범위를 구할 떄는 [[]]")
print(df.loc[['037730', '036360']])
print(df.iloc[[0, 2]], end='\n\n')

df = df.loc[['037730', '036360']]
print(df[['종목명', '현재가']], end='\n\n')

print("df.loc[['037730', '036360'], ['종목명', '현재가']]")
print(df.loc[['037730', '036360'], ['종목명', '현재가']], end='\n\n')

print("df.iloc[[0, 1], [0, 1]]")
print(df.iloc[[0, 1], [0, 1]], end='\n\n')


data1 = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005760", "ACTS", 1185]
]
columns1 = ["종목코드", "종목명", "현재가"]
df1 = DataFrame(data=data1, columns=columns1)
df1 = df1.set_index("종목코드")

cond = df1['현재가'] >= 1400
print("조건별 출력")
print(df1.loc[cond, "종목명"], end='\n\n')
print(df1.loc[cond, "현재가"])




