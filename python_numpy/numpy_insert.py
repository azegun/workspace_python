import numpy as np

arr1 = np.arange(1, 11)
print(arr1)
print("arr1_insert shaper > ", arr1.shape, end='\n\n')

arr1_insert = np.insert(arr1, 0, 1024)
print(arr1_insert)
print("arr1_insert shape > ", arr1_insert.shape, end='\n\n')

arr2 = np.array([[1, 2], [3, 4]])
print(arr2, end='\n\n')

# reshape로 배열 재정의해서 사이즈 만들고, 추가 - 사용에 어려움은 있음
arr2_insert = np.insert(arr2, (4, 4), 200).reshape(2, 3)
print("arr2_insert.shape >>", arr2_insert.shape)
arr2_insert[1][0] = 200      # index로 지정해서 업데이트하기
print(arr2_insert, end='\n\n')

# axis로 행, 열 구분해서 추가하기.
arr2_axis = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2_axis, end='\n\n')
arr2_axis_insert = np.insert(arr2_axis, 2, 100, axis=0)   # axis = 0 은 row값 가로 axis = 1은 cols 세로
print(arr2_axis_insert)

