import numpy as np

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2, end='\n\n')

# 2번쨰 배열까지 100으로 수정
arr2[0, :3] = 100
print(arr2, end='\n\n')

arr1 = np.arange(10)
print(arr1, end='\n\n')

# 삭제하고 싶은 배열, 위치
arr1_delete = np.delete(arr1, 0) 
print(arr1_delete, end='\n\n')

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2, end='\n\n')
arr2_delete_row = np.delete(arr2, 2, axis=0)
print(arr2_delete_row, end='\n\n')

arr2_delete_cols = np.delete(arr2, 1, axis=1)
print(arr2_delete_cols, end='\n\n')