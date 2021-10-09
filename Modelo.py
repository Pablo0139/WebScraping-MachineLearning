import pandas as pd

tabla  = pd.read_csv(r'C:\Users\pablo\Desktop\UCLM\4º\TFG\Virtual\cultura\cultura_cuerpo2.csv', sep = ';')
tabla = tabla.sample(frac=1).reset_index(drop=True)

n_muestras = 2159
x_train = tabla['cuerpo']
x_train = x_train.iloc[0:n_muestras]
y_train = tabla['clasificacion']
y_train = y_train.iloc[0:n_muestras]

x_test = tabla['cuerpo']
x_test = x_test.iloc[n_muestras:]
y_test = tabla['clasificacion']
y_test = y_test.iloc[n_muestras:]

print('x_train', x_train[0])
print('y_train', y_train[0:5])

from keras.preprocessing.text import Tokenizer

max_words = 10000

tokenizer = Tokenizer(num_words=max_words)

tokenizer.fit_on_texts(x_train)
tokenizer.fit_on_texts(x_test)

m_list = ['binary','count','freq','tfidf']
m = m_list[0]
print(m) 
x_train = tokenizer.texts_to_matrix(x_train, mode = m)
x_test  = tokenizer.texts_to_matrix(x_test,  mode = m)

tokenizer = Tokenizer()

tokenizer.fit_on_texts(y_train)
tokenizer.fit_on_texts(y_test)

y_train = tokenizer.texts_to_matrix(y_train, mode = m)
y_test  = tokenizer.texts_to_matrix(y_test,  mode = m)

num_classes = len(y_train[0])

print('x_train', x_train[0])
print('l.x_train', len(x_train[0]))

print('y_train', y_train[0])
print('l.y_train', len(y_train[0]))

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

model = Sequential()
model.add(Dense(220, input_shape=(max_words,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.metrics_names)

batch_size = 32
epochs = 3

history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.1)
score = model.evaluate(x_test, y_test, batch_size=batch_size, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
