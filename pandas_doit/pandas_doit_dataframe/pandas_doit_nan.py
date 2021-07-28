import pandas as pd


evola = pd.read_csv('../pandas_doit_dataframe/data/country_timeseries.csv')
print(evola.isnull().sum(), end='\n\n')

evola_parts = evola.iloc[:10, :5]  # [행, 열]
# ffill - front, bfill - back,
print(evola_parts.fillna(method='bfill'), end='\n\n')  # NaN값을 0으로 채운다는 메서드

# 앞의 값과 뒤의 값의 비교를 통해 중간에 평균값을 입력
print(evola_parts.interpolate(), end='\n\n')

# NaN 값을 삭제
print(evola_parts.dropna(), end='\n\n')

three_country = evola.loc[:10, ['Cases_Guinea',
                                'Cases_Liberia',
                                'Cases_SierraLeone']]
print(three_country, end='\n\n')

# NaN값이 있는채로 더하면 NaN값이 있다면 NaN으로 자동 출력
evola['country_sum'] = evola['Cases_Guinea'] \
                       + evola['Cases_Liberia']\
                       + evola['Cases_SierraLeone']

print(evola[['Cases_Guinea', 'Cases_Liberia',
             'Cases_SierraLeone', 'country_sum']], end='\n\n')

# NaN값을 0으로 치환 후 전체 더함.
nan_three_country = three_country.fillna(0)
print(nan_three_country, end='\n\n')

nan_three_country['country_sum'] = nan_three_country['Cases_Guinea'] \
                                   + nan_three_country['Cases_Liberia']\
                                   + nan_three_country['Cases_SierraLeone']

print(nan_three_country)

# NaN에다가 평균값을 채움.
evola_parts_ex = evola.iloc[:10, :5]
print(evola_parts_ex, end='\n\n')
evola_parts_Cases_Guinea = evola_parts_ex.fillna(evola_parts_ex.mean())
print(evola_parts_Cases_Guinea, end='\n\n')