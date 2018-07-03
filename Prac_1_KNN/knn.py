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

clf = KNeighborsClassifier(n_neighbors = 3)
clf.fit(x_train, y_train)

c = clf.predict(x_test)

from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, c)
print(score)
