from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

import numpy as np

x_train = np.resize(x_train, (60000,784))
x_test = np.resize(x_test, (10000, 784))

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors = 3)
clf.fit(x_train, y_train)

c = clf.predict(x_test)

from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, c)
print(score)