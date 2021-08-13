import tensorflow as tf
import numpy as np

c = tf.constant([[4.0, 5.0], [10.0, 1.0]])

# 배열 안에서 가장 큰 값
print(tf.reduce_max(c))

# index 중에 가장 큰 인덱스의 값
print(tf.argmax(c))

# 소프트 맥스로 계산해주기
print(tf.nn.softmax(c), end='\n\n')

# [batch, width, height, features]
rank_4_tensor = tf.zeros([3, 2, 4, 5])

print(rank_4_tensor, end='\n\n')

# 모든 타입
print(rank_4_tensor.dtype, end='\n\n')
# 배열안의 구조가 몇 종류
print(rank_4_tensor.ndim, end='\n\n')
# 배열의 형태
print(rank_4_tensor.shape, end='\n\n')
# 0번쨰 배열의원소
print(rank_4_tensor.shape[0], end='\n\n')
# 맨 뒤에 배열의원소
print(rank_4_tensor.shape[-1], end='\n\n')
# 사이즈 and numpy로 변경
print(tf.size(rank_4_tensor).numpy(), end='\n\n')
