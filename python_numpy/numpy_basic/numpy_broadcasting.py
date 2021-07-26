import numpy as np

row = np.arange(2, 10)
attr = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])

result = row * attr

print(result.T.shape)

print(result.T, end='\n\n')  # .T 행열을 반대로

print("total >>", result.sum())
print("average >>", result.mean())
print("shape>>", result.shape)
print("type>>", result.dtype, end='\n\n')

result_float = np.array(result, dtype=float)
print(result_float, end='\n\n')
print(result * 0.1)




