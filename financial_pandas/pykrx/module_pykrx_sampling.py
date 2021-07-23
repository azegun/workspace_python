from pykrx import stock

df = stock.get_market_ohlcv_by_date("20180101", "20180531", "005930")
print(df)

df_basic = stock.get_market_ohlcv_by_date("20180101", "20180131", "005930")
# resample('M') 메서드는 월 단위로 데이터를 모읍니다.
# first() 메서드는 월 단위 데이터에서 첫 번째 데이터를 대푯값
# last() 메서드는 월 단위 데이터에서 마지막날
# resample("MS") 대푯값을 첫날로, resample("M") 대푯값을 마지막날
mon = df.resample("MS").first()
print(mon)

# 각각의 칼럼(시가/종가/고가/저가/거래량)에 다른 기준을 적용하기 위해 apply() 메서드를 사용
how = {
    '시가': 'first',    # 옵션들을 적용
    '종가': 'last',
    '고가': 'max',
    '저가': 'min',
    '거래량': 'sum'
}

mon = df.resample('MS').apply(how)
print(mon)


