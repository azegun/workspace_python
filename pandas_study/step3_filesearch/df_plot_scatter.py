import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 한글 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 맑은 고딕으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./auto-mpg.csv', header=None)  # 데이터프레임 변환

pd.set_option('display.max_columns', len(df.columns))
pd.set_option('display.max.colwidth', 30)
pd.set_option('display.width', 1000)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
              'weight', 'acceleration', 'model year', 'origin', 'name']

print("auto-mpg", df.head(), sep='\n', end='\n\n')

# 2개의 열을 선택하여 산점도 그리기
df.plot(x='weight', y='mpg', kind='scatter', title='무게(weight)와 연비(mpg)의 관꼐')
plt.show()

