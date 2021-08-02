import pandas as pd

ebola = pd.read_csv('../pandas_doit_dataframe/data/country_timeseries.csv')
ebola['new_Date'] = pd.to_datetime(ebola['Date'])
ebola['date_Year'] = ebola['new_Date'].dt.year   # 년도만 출력
ebola['date_Month'] = ebola['new_Date'].dt.month
ebola['date_Day'] = ebola['new_Date'].dt.day

print(ebola[['Date', 'new_Date', 'date_Year', 'date_Month', 'date_Day']])

ts = pd.date_range(start='2021-01-01',
                   end=None,
                   periods=12,  # 생성할 timestamp 수
                   freq='M',   # 시간주기(Month Start) 'D' - day, 'W' - week
                   tz='Asia/Seoul')     # 원하는 시간대(Time Zone)
print(ts)

data = ['3% 상승', '1% 상승', '3% 하락',
        '4% 상승', '2% 상승', '4% 하락',
        '5% 상승', '3% 상승', '5% 하락',
        '6% 상승', '4% 상승', '6% 하락']

Series_data = pd.Series(data=data, index=ts)
print(Series_data)