import numpy as np

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(arr, type(arr), end='\n\n')

print(arr[2], arr[4], end='\n\n')

data = [11, 22, 33, 44]
arr1 = np.array(data)
print(arr1, type(arr1))

# update
arr1[0] = 100
print(arr1, end='\n\n')

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2, end='\n\n')

# [0][0] 엘리먼트 뽑기
zeroToZero = arr2[0, 0]
print(zeroToZero, end='\n\n')

# [1][1], [2][2] 엘리먼트 뽑기
oneToTwo = arr2[1, 1]
twoToTow = arr2[2, 2]
print(oneToTwo, twoToTow, end='\n\n')

# 3차원 배열
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 20, 30], [40, 50, 60], [70, 80, 90]],
    [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
    ])
print("3차원 배열")
print(arr3)

# 3차원 배열 인덱스
# 9, 50, 700 출력
print(arr3[0, 2, 2], arr3[1, 1, 1], arr3[2, 2, 0])
print(arr3[2, 2, 2], arr3[0, 1, 2])



