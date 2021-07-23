from pykrx import stock
# 298540 - 더네이쳐홀딩스, 011200 - HMM, 003490 - 대한항공, 017960 - 한국카본
# 012330 - 현대모비스,  005387 - 현차2우b , 066575 - LG전자우
# 035420 - NAVER, 035720 -카카오, 017670- sk텔레콤
# 005930 - 삼성전자, 000660- 하이닉스
# 051900 - LG생활건강
# 352820 - 하이브, 035900 - jyp, 041510 - sm, 122870 - yg

df = stock.get_market_ohlcv_by_date("20180101", "20180531", "005930")
print(df)
df['5일이동평균'] = df['종가'].rolling(window=5).mean()  # pandas에서 사용하는 rolling 5개 선택 mean() 평균

# 평균과 시가를 맞춰줘야하니 평균에 (1)하면 다음날 시가 or 시가에(-1)하면 전날 평균 맞혀준다.
cond = df['5일이동평균'].shift(1) < df['시가']
print("평균보다 상승시작", len(df[cond]))
print("영업일", len(df))