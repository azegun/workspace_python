from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print("load >>", (x_train, y_train), (x_test, y_test))

X_train = x_train.reshape(60000, 784)
X_test = x_test.reshape(10000, 784)


X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255

Y_train = to_categorical(y_train, 10)
Y_test = to_categorical(y_test, 10)

model = Sequential()
# 층을 추가해줌
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu'))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
# 보고서
# model.summary()

# loss - 원핫코딩으로 뽑는다
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# verbose 0 : 함수의 결과값 출력 x, 1 : 결과값, 2 : 학습값
model.fit(X_train, Y_train, batch_size=128,
          epochs=10, verbose=1)

predicted_classes = np.argmax(model.predict(X_test),
                              axis=1)
correct_indices = np.nonzero(predicted_classes ==
                             y_test)[0]
incorrect_indices = np.nonzero(predicted_classes !=
                               y_test)[0]

plt.figure()
for i in range(9):
    plt.subplot(3, 3, i+1)
    correct = correct_indices[0]
    plt.imshow(X_test[correct].reshape(28, 28), cmap='gray')
    plt.title('Predicted {}, Class {}'.format(predicted_classes[correct],
                                              y_test[correct]))
plt.tight_layout()
plt.show()


# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)