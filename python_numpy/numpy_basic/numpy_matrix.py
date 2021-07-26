import numpy as np

arr2 = np.array([[1, 2], [3, 4]])
print(arr2, end='\n\n')

# [[1. 0.]
#  [0. 1.]]
unitMatrix = np.eye(2)
print(unitMatrix, end='\n\n')

print(arr2 * unitMatrix, end='\n\n')  # [[1. 0.][0. 4.]]

# step 값 출력
arr1 = np.arange(1, 30, 3)
print("step arange 출력")
print(arr1, end='\n\n')

# 100포함 범위 5등분해주세요.
arr_lin = np.linspace(1, 100, 5)
print("lin 출력")
print(arr_lin, end='\n\n')

# random 출력
arr_random = np.random.random((3, 3))
print(arr_random, end='\n\n')

# randint 출력  - 10이랑 100 포함 (2, 5)사이즈 행렬 출력
arr_int = np.random.randint(10, 100, (2, 5))
print(arr_int, arr_int[1, 3], type(arr_int[1, 3]), end='\n\n')


arr_int1 = np.random.randint(1, 100, (5, 5))
print(arr_int1)
print("3행 3열 >> ", arr_int1[2, 2])

arr_int2 = np.random.randint(1, 100, (3, 3, 3))
print(arr_int2, end='\n\n')
print("2번쨰 행렬 0행 2열 >> ", arr_int2[1, 0, 1], end='\n\n')
print("최대값 >>", arr_int2.max(), "최소값 >>", arr_int2.min(), "평균값 >>", arr_int2.mean())

arr_full = np.full((2, 5), 30)
print(arr_full)

