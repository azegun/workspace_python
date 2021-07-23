from pandas import DataFrame
# 데이터 프레임은 동일한 인덱스를 갖는 여러 시리즈 객체가 붙어 있는 구조.
# 데이터 프레임을 구성하는 시리즈는 동일 인덱스를 갖는다.

# 리스트와 딕셔너리로 생성 (컬럼은 리스트, key는 딕셔너리)
data = {
    '종목코드': ['037730', '036360', '005760'],
    '종목명': ['3R', '3SOFT', 'ACTS'],
    '현재가': [1510, 1790, 1185]
}

df = DataFrame(data)
print(df, type(df), end='\n\n')

# 리스트로 생성
data_list = [
    ['037730', '3R', 1510],
    ['036360', '3SOFT', 1790],
    ['005760', 'ACTS', 1185]
]

columns = ['종목코드', '종목명', '현재가']

df_list = DataFrame(data=data_list, columns=columns)
print("리스트로 생성")
print(df_list, end='\n\n')

# 딕셔너리로 생성
data_dic = [
    {'종목코드': '037730', '종목명': '3R', '현재가': 1510},
    {'종목코드': '036360', '종목명': '3SOFT', '현재가': 1790},
    {'종목코드': '005760', '종목명': 'ACTS', '현재가': 1185}
]

df_dic = DataFrame(data_dic)
print("dic으로 만듬")
print(df_dic)