from pykrx import stock
import numpy as np

import pandas as pd
# 298540 - 더네이쳐홀딩스, 011200 - HMM, 003490 - 대한항공, 017960 - 한국카본
# 012330 - 현대모비스,  005387 - 현차2우b , 066575 - LG전자우
# 035420 - NAVER, 035720 -카카오, 017670- sk텔레콤
# 005930 - 삼성전자, 000660- 하이닉스
# 051900 - LG생활건강
# 352820 - 하이브, 035900 - jyp, 041510 - sm, 122870 - yg

# df = stock.get_market_ohlcv_by_date("20190101", "20210722", "035720")
# print(df)
#
# df["전날거래량"] = df["거래량"].shift(1) # row를 한칸 뒤로 미루기
# compare_amount = df['거래량'] > df['전날거래량']
#
# print("전날거래량 추가")
# print(df[compare_amount], end='\n\n')
#
# print('상승일', len(df[compare_amount]))
# print('영업알', len(df))

# df = df.astype({'전날거래량': np.int64}) # astype으로 정수값으로 변경

df1 = stock.get_market_ohlcv_by_date("20180101", "20180531", "005930")

print("df1['종가'] > df1['시가'] test")
cond = df1['종가'] > df1['시가'].shift(-1)  # -1을 넣으면 시작가가 상승했는지 확인가능
print("상승시작 >>", len(df1[cond]))  # 상승장 일
