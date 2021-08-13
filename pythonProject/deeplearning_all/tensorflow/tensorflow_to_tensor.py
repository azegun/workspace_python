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
print("tensor>> ", d_numpy_to_tensor, type(d_numpy_to_tensor), end='\n\n')

the_f64_tensor = tf.constant([2.2, 3.3, 4.4], dtype=tf.float64)
the_f16_tensor = tf.cast(the_f64_tensor, dtype=tf.float16)
the_u8_tensor = tf.cast(the_f16_tensor, dtype=tf.uint8)
print(the_f64_tensor)
print(the_f16_tensor)
print(the_u8_tensor, end='\n\n')

# 곱 or 덧셈
x = tf.constant([1, 2, 3])
y = tf.constant(2)
z = tf.constant([2, 2, 2])

print(tf.multiply(x, 2))
print(x * y)
print(x * z, end='\n\n')

x_reshape = tf.reshape(x, [3, 1])
y_range = tf.range(1, 5)

print(x_reshape, '\n')
print(y_range, '\n')
print(tf.multiply(x_reshape, y_range), end='\n\n')

# 브로드캐스팅 [[1 2 3] [1 2 3], [1 2 3]]
print(tf.broadcast_to(tf.constant([1, 2, 3]), [3, 3]))

# 비정형 tensor

ragged_list = [
    [0, 1, 2, 3],
    [4, 5],
    [6, 7, 8],
    [9]
]

try:
    tensor = tf.constant(ragged_list)
except Exception as e:
    print("111")
    print(f'{type(e).__name__}: {e}')

# 알수 없는 형상으로 (4, None)
ragged_tensor = tf.ragged.constant(ragged_list)
print(ragged_tensor.shape)

# 문자열 split
tensor_of_strings = tf.constant(['Gray wolf', 'Quick brown fox', 'Lazy dog'])
print(tensor_of_strings, end='\n\n')

tensor_of_strings_split = tf.strings.split(tensor_of_strings)
print(tensor_of_strings_split, tensor_of_strings_split.shape, end='\n\n')

# string >> number
text = tf.constant("1 10 100")
print(tf.strings.to_number(tf.strings.split(text, " ")))

# tf.cast를 사용하여 문자열 텐서를 숫자로 변환할 수는 없지만,
# 바이트로 변환한 다음 숫자로 변환할 수 있습니다.

unicode_bytes = tf.constant("アヒル 🦆")
unicode_char_bytes = tf.strings.unicode_split(unicode_bytes, "UTF-8")
unicode_values = tf.strings.unicode_decode(unicode_bytes, "UTF-8")

print("\nUnicode bytes:", unicode_bytes)
print("\nUnicode chars:", unicode_char_bytes)
print("\nUnicode values:", unicode_values)

# 희소한 경우에는 sparse
sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]],
                                       values=[1, 2],
                                       dense_shape=[3, 4])

print(sparse_tensor, '\n')
print(tf.sparse.to_dense(sparse_tensor))