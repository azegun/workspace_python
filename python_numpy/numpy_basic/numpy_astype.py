import numpy as np

arr1 = np.array(['1.5', '2', '2.7', '4'])
print(arr1, arr1.dtype)

# int 안됨 유니코드에서 바로안됨 플로트로 만들었다가 int로
change_arr1 = arr1.astype(float)
print(change_arr1, change_arr1.dtype)

change_int = change_arr1.astype(int)
print(change_int, change_int.dtype)

arr1 = np.array([1, 2, 3, 4])
print(arr1, arr1.dtype)

# array만들면서 바로dtype변경으로 타입 변경가능
arr1_str = np.array(['1.5', '2', '2.7', '4'], dtype=float)
print(arr1_str.astype(int))
