from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

import pandas as pd
import numpy
import os
import tensorflow as tf
import matplotlib.pyplot as plt

seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

df_pre = pd.read_csv('../dataset/wine.csv', header=None)
df = df_pre.sample(frac=0.15)


dataset = df.values
X = dataset[:, 0:12].astype(float)
Y = dataset[:, 12]

model = Sequential()
model.add(Dense(30, input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


# model 저장
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

modelpath = './model/{epoch:02d}-{val_loss:.4f}.hdf5'
checkpointer = ModelCheckpoint(filepath=modelpath,
                               monitor='val_loss',
                               verbose=1,
                               save_best_only=True)

# 자동 학습 중단
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=100)

model.fit(X, Y, validation_split=0.2,
          epochs=2000, batch_size=500,
          callbacks=[early_stopping_callback, checkpointer])
# matplot
# hist = model.fit(X, Y,
#                     validation_split=0.33,
#                     epochs=3500,
#                     batch_size=500)
#
# y_vloss = hist.history['val_loss']
#
# y_acc = hist.history['accuracy']
#
# x_len = numpy.arange(len(y_acc))
# plt.plot(x_len, y_vloss, 'o', c='red', markersize=3)
# plt.plot(x_len, y_acc, 'o', c='blue', markersize=3)
#
# plt.show()

print('\n Accuracy : %.4f' % (model.evaluate(X, Y)[1]))
