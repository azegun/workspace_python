from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import load_model

seed = 0
np.random.seed(seed)
tf.random.set_seed(3)

df = pd.read_csv('../dataset/sonar.csv', header=None)

dataset = df.values

X = dataset[:, 0:60].astype(float)
Y_obj = dataset[:, 60]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

# 학습셋과 테스트셋 구분
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

model = Sequential()
model.add(Dense(24, input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=130, batch_size=5)

model.save('my_model3.h5')

# 테스트를 위해 메모리 내의 모델을 삭제
del model
model = load_model('my_model3.h5')
print(model)

print('\n Test Accuracy: %.4f' % (model.evaluate(X_test, Y_test)[1]))