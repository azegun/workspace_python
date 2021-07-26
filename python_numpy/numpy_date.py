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