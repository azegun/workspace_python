import tensorflow as tf
import numpy as np

var_x = tf.Variable(tf.constant([[1], [2], [3]]))
print(var_x, end='\n\n')
print(var_x.shape, type(var_x))

# tensor Variable >> list
var_x_as_list = var_x.shape.as_list()

print("list >>>", var_x_as_list,
      type(var_x_as_list), end='\n\n')

# [3, 1] >> [1, 3]
reshaped = tf.reshape(var_x, [1, 3])
print(reshaped, type(reshaped))

rank_3_tensor = tf.constant([
  [[0, 1, 2, 3, 4],
   [5, 6, 7, 8, 9]],
  [[10, 11, 12, 13, 14],
   [15, 16, 17, 18, 19]],
  [[20, 21, 22, 23, 24],
   [25, 26, 27, 28, 29]],])

print(rank_3_tensor, end='\n\n')

# tensor >> flatten만들기  [-1]이 중요
rank_3_tensor_flatten = tf.reshape(rank_3_tensor, [-1])
print(rank_3_tensor_flatten)

rank_3_tensor_reshape = rank_3_tensor
print(tf.reshape(rank_3_tensor_reshape, [3 * 2, 5]), end='\n\n')
print(tf.reshape(rank_3_tensor_reshape, [3, -1]), end='\n\n')

# 왜 오류가 날까?
print("1 ", tf.reshape(rank_3_tensor_reshape, [2, 3, 5]), end='\n\n')
print("2 ", tf.reshape(rank_3_tensor_reshape, [5, 6]), end='\n\n')

# 범위를 작게 reshape 함 에러
try:
    tf.reshape(rank_3_tensor_reshape, [7, -1])
except Exception as e:
    print("3", f'{type(e).__name__}: {e}')


