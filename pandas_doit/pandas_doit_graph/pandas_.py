import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

df = pd.read_excel('../pandas_doit_graph/data/시도별 전출입 인구수.xlsx', header=0)
print(df, end='\n\n')

# 내장되어 있는 폰트로 변경.
font_path = '../pandas_doit_graph/data/H2GTRM.TTF'

font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
df = df.fillna(method='ffill')
print(df, end='\n\n')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')

df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

print(df_seoul)

daegu = df_seoul.loc['대구광역시']
print(daegu)

plt.plot(daegu)
plt.title('서울 -> 대구로 인구 이동 ')
plt.xlabel('기간')
plt.ylabel('이동 인구수')

plt.show()