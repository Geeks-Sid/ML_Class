fil_loc = r'C:\Users\oslab\Downloads\mnist.pkl.gz'
import pickle
#train_set, valid_set, test_set = pickle.load(fil_loc)

import sys
import gzip
with gzip.open(fil_loc, 'rb') as f:
    if sys.version_info.major > 2:
        train_set, valid_set, test_set = pickle.load(f, encoding='latin1')
    else:
        train_set, valid_set, test_set = pickle.load(f)
from sklearn.neighbors import KNeighborsClassifier

x_train = train_set[0]
y_train = train_set[1]
x_test = test_set[0]
y_test = test_set[1]
x_train = x_train[:6000]
import math
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import time
class simple_knn():
    def __init__(self):
        pass

    def train(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X, k=1):
        dists = self.compute_distances(X)
        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)

        for i in range(num_test):
            k_closest_y = []
            labels = self.y_train[np.argsort(dists[i,:])].flatten()
            k_closest_y = labels[:k]
            c = Counter(k_closest_y)
            y_pred[i] = c.most_common(1)[0][0]

        return(y_pred)

    def compute_distances(self, X):
        num_test = X.shape[0]
        num_train = self.X_train.shape[0]

        dot_pro = np.dot(X, self.X_train.T)
        sum_square_test = np.square(X).sum(axis = 1)
        sum_square_train = np.square(self.X_train).sum(axis = 1)
        dists = np.sqrt(-2 * dot_pro + sum_square_train + np.matrix(sum_square_test).T)

        return(dists)

batch_size = 2000
k = 3
#k = 1
classifier = simple_knn()
classifier.train(x_train, y_train)
classifier.predict(x_test)