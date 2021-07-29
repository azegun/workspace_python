import pandas as pd

# 모든 행, 열들을 보이게하기
pd.set_option('max_columns', None)
# pd.set_option('max_rows', None)

pew = pd.read_csv('../pandas_doit_dataframe/data/pew.csv')
bilboard = pd.read_csv('../pandas_doit_dataframe/data/billboard.csv')
weather = pd.read_csv('../pandas_doit_dataframe/data/weather.csv')

# print(pew, end='\n\n')

# 고정 시킬 열을 지정 (가로로 늘여진게 세로로 가독성 좋게 표현)
# var_name, value_name 컬럼명 변경
melt_pew = pd.melt(pew, id_vars='religion',
                    var_name='income',
                    value_name='count')
# print(melt_pew)

# print(bilboard, end='\n\n')

melt_bilboard = pd.melt(bilboard,
                        id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                        var_name='week',
                        value_name='rating')

# booleam 조건을 통한 출력
# print(melt_bilboard[melt_bilboard['track'] == 'Loser'])

# duplicates하게되면 중복값들은 삭제
bilboard_songs = melt_bilboard[['year', 'artist', 'track', 'time', 'date.entered']]
bilboard_songs = bilboard_songs.drop_duplicates()
print(bilboard_songs)

# print(weather, end='\n\n')
melt_weather = pd.melt(weather,
                       id_vars=['id', 'year', 'month', 'element'],
                       var_name='day',
                       value_name='temperature')

# print(melt_weather, end='\n\n\n\n')


new_weather = melt_weather.pivot_table(index=['id', 'year', 'month', 'day'],
                                       columns='element',
                                       values='temperature',
                                       dropna=False
                                       )

# index가 지저분하게 산발되어있을경우 reset_index()로 정리해준다.
# print(new_weather.reset_index())

