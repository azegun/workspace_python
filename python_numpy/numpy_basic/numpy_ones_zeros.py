import numpy as np

arr1 = np.arange(64)
print(arr1)
print("=========================================")

arr2 = arr1.reshape(4, 16)
print(arr2)

print("=========================================")
arr3 = arr1.reshape(2, 16, 2)
print(arr3)

zero = np.zeros((5, 5, 5))
print(zero, end='\n\n')

one = np.ones((5, 3, 5))
print(one, one.dtype)