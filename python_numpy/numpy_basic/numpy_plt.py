import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 1, 5)   # 0에서 1까지 5등분
# print(a)
# plt.hist(a)   # 막대 그래프
# plt.plot(a, 'x')   # 직선 그래프
# plt.show()

# np.save("./my_array1", a)

arr = np.arange(64)
print(arr.ndim)  # 몇차원 행렬인지 알려줌
arr2 = arr.reshape(4, 16)
print(arr2.ndim)