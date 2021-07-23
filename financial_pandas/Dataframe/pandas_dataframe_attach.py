from pandas import DataFrame
import pandas as pd
# 첫번째 데이터프레임
data1 = {
    '종가': [113000, 111500],
    '거래량': [555850, 282163]
}
index1 = ['2019-06-21', '2019-06-20']
df1 = DataFrame(data=data1, index=index1)
print(df1)

data2 = {
    '종가': [111000, 109000],
    '거래량': [483689, 791946]
}
index2 = ['2019-06-19', '2019-06-18']
df2 = DataFrame(data=data2, index=index2)
print(df2, end='\n\n')

df_append = df1.append(df2)
print("2개의 DataFrame을 append로 붙임")
print(df_append, end='\n\n')

print("2개의 DataFrame을 concat로 붙임")
df_concat = pd.concat([df1, df2])
print(df_concat, end='\n\n')

data_left = {
    '종가': [113000, 111500],
    '거래량': [555850, 202163]
}
index_date = ['2019-06-21', '2019-06-20']
df_left = DataFrame(data=data_left, index=index_date)
print(df_left)

data_right = {
    '시가': [112500, 110000],
    '고가': [115000, 112000],
    '저가': [111500, 109000]
}

df_right = DataFrame(data=data_right, index=index_date)
print(df_right, end='\n\n')

#  axis=1 옵션을 통해 좌우로 이어 붙인다는 것을 알려줌
df_total = pd.concat([df_left, df_right], axis=1)
print(df_total, end='\n\n')

print("컬럼 순서변경")
refact_columns = ['시가', '고가', '저가', '종가', '거래량']
df_total = df_total[refact_columns]
print(df_total, end='\n\n')

print("excel")
df_total.to_excel('data.xlsx', sheet_name='종가', index=False)
df_excel = pd.read_excel("data.xlsx")
print("read success")



