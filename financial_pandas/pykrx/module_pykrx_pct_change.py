import pandas as pd
from pykrx import stock

data = {'삼성전자': [52200, 52300, 52900, 52000, 51700],
           'LG전자': [68200, 67800, 68800, 67500, 66300]}

df = pd.DataFrame(data=data)
print(df.pct_change())
print()
print(df.pct_change()*100)   # 수익률 계싼해주는 메서드
print()

# 기존에 2틀 전 데이터 찾아오기
print(df.pct_change(periods=2)*100)

