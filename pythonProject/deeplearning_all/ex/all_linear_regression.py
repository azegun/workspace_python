import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [[2, 81], [4, 93], [6, 91], [8, 97]]

x = [i[0] for i in data]
y = [i[1] for i in data]

plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

x_data = np.array(x)
y_data = np.array(y)

a = 0
b = 0

# 학습률 정하기
lr = 0.03

# 몇 번 반복될지
epochs = 2001

# 경사 하강법
for i in range(epochs):
    y_pred = a * x_data + b  # y를 구하는 식
    error = y_data - y_pred
    # 오차 함수를 a로 미분한 값
    a_diff = -(2/len(x_data)) * sum(x_data * (error))
    # 오차 함수를 b로 미분한 값
    b_diff = -(2/len(y_data)) * sum(error)

    a = a - lr * a_diff   # 학습율을 곱해 기존의 a값 업데이트
    b = b - lr * b_diff   # 학습율을 곱해 기존의 b값 업데이트

    if i % 100 == 0:
        print('epoch=%.f, 기울기=%.04f, 절편=%.04f' % (i, a, b))


y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()


