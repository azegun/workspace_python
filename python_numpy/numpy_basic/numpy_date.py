import numpy as np

date = np.array('2021-01-01', dtype=np.datetime64)
print(date)

new_date = date + np.arange(30)
print(new_date, end='\n\n')
print("date 배열의 shape 확인 (1차원 30개) >> ", new_date.shape, end='\n\n')

arr2 = np.array([[1, 2], [3, 4]])
print("arr2 2차원 배열 shape>> ", arr2.shape, end='\n\n')

arr1 = np.arange(64)
arr3 = arr1.reshape(4, 4, 4)
print("=========reshape=======")
print(arr3, end='\n\n')
print("arr3 3차원 배열 shape>> ", arr3.shape)

h1 = np.datetime64('2021-07-26 12')   # 시간까지
h2 = np.datetime64('2021-07-27 12')
m1 = np.datetime64('2021-07-26 12:00') # 분까지
m2 = np.datetime64('2021-07-27 12:00')
s1 = np.datetime64('2021-07-26 12:00:00') # 초까지
s2 = np.datetime64('2021-07-27 12:00:00')

time = np.datetime64('2021-06-21 12:00:00')
time1 = np.datetime64('2021-07-26 12:30:00')

print(time1 - time)

print(h2 - h1)
print(m2 - m1)
print(s2 - s1, end='\n\n')

print("추석까지 남은 days(today = 2021-07-26)")
time_tanks_Gday = np.datetime64('2021-09-21')
today = np.datetime64('2021-07-26')
print(time_tanks_Gday-today)
