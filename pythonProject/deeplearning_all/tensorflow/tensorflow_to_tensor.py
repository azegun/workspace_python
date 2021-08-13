import tensorflow as tf
import numpy as np

tf.__version__
'2.2.0'

# 상수 정의
a = tf.constant(10)
b = tf.constant(20)

# c = tensor
c = a + b
print(type(c))

# d = numpy.int32
d = (a + b).numpy()


print(type(d), d)
print(c)

# to_tensor
d_numpy_to_tensor = tf.convert_to_tensor(d)
print("tensor>> ", d_numpy_to_tensor, type(d_numpy_to_tensor))
