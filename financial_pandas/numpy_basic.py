import numpy as np
data = [1, 2, 3]
new_data =[]

for x in data:
    new_data.append(x * 10)
print(new_data)

data1 = [1, 2, 3]
arr = np.array(data1)
data2 = arr * 10
print(data2, type(data2))  # [10 20 30] <class 'numpy.ndarray'>  (행렬연산에 특화된 numpy)

# 5일간의 고가와 저가 빼기  np.array로 하면 배열이라서 계산이 쉬움

high = [92700, 92400, 92100, 94300, 92300]
low = [90000, 91100, 91700, 92100, 90900]

arr_high = np.array(high)
arr_low = np.array(low)

arr_diff = arr_high - arr_low
print("high - low :", arr_diff)

