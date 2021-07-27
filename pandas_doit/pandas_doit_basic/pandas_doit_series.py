import numpy as np
import pandas as pd

exam = ['김지용', 20]
exam_index = ['name', 'age']
make_series = pd.Series(exam, exam_index)
print(make_series)

data = {'NAME': ['태연', '제니', '유주'],
        'GROUP': ['소시', '블핑', '걸프'],
        'BORN': ['1989-03-09', '1996-01-16', '1997-10-04'],
        'AGE': [33, 26, 25],
        'COMPANY': ['SM', 'YG', 'S_M']}
index = ['1번', '2번', '3번']
make_DateFrame = pd.DataFrame(data=data, index=index)
print(make_DateFrame)
print(make_DateFrame.loc['1번'], end='\n\n')

age = make_DateFrame['AGE']
print("=======================")
print('AGE의 평균값: ', age.mean())
print('AGE의 최댓값: ', age.max())
print('AGE의 최솟값: ', age.min())
print('AGE의 표준편차값: ', age.std(), end='\n\n')

describe = make_DateFrame.describe()  # 기본 중요한 값들 출력
print(describe)



