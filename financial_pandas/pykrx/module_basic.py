from pykrx import stock
# 298540 - 더네이쳐홀딩스, 011200 - HMM, 003490 - 대한항공, 017960 - 한국카본
# 012330 - 현대모비스,  005387 - 현차2우b , 066575 - LG전자우
# 035420 - NAVER, 035720 -카카오, 017670- sk텔레콤
# 005930 - 삼성전자, 000660- 하이닉스
# 051900 - LG생활건강
# 352820 - 하이브, 035900 - jyp, 041510 - sm, 122870 - yg
# 액분 전 가격 adjusted = False
df_samsung = stock.get_market_ohlcv_by_date("20100720", "20210722", "005930", adjusted = False)  # 날짜별 종목검색 n+1 ~ n
# print(df_samsung, end='\n\n')
print(df_samsung)
print(df_samsung['등락률'])

# print("종가 추출")
# print(df.loc['20210721']['종가'])
# print(df.loc['20210721', '종가'])
# print(df.iloc[1][3])
# print(df.iloc[1, 3], end='\n\n')
# print("비교 수치")
# compare = df_samsung['종가'] < 50000  # 5만전자
# print("5만전자")
# print(df_samsung[compare])
# compare = df['종가'] > df['시가']

# print(df[compare])

df_kakao = stock.get_market_ohlcv_by_date("20100720", "20210722", "035720")
