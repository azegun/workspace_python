import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])

print(sr)
print()
print(sr[0])
print(sr['이름'])

#여러개의 원소를 선택(인덱스 리스트 활용)
print(sr[[1, 2]])
print('\n')
print(sr[['생년월일', '성별']])

#여러 개의 원소를 선택(인덱스 범위 지정)
print(sr[1: 2])
print('\n')
print(sr['생년월일': '성별'])