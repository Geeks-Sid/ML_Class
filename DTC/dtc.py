import pandas as pd
from sklearn.model_selection import train_test_split
column = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'status']
df = pd.read_csv('cars.csv', header = None)
df.columns = column

df['buying'] = df['buying'].astype('category')
df['buying'] = df['buying'].cat.codes

df['maint'] = df['maint'].astype('category')
df['maint'] = df['maint'].cat.codes

df['doors'] = df['doors'].astype('category')
df['doors'] = df['doors'].cat.codes

df['persons'] = df['persons'].astype('category')
df['persons'] = df['persons'].cat.codes

df['lug_boot'] = df['lug_boot'].astype('category')
df['lug_boot'] = df['lug_boot'].cat.codes

df['safety'] = df['safety'].astype('category')
df['safety'] = df['safety'].cat.codes

df['status'] = df['status'].astype('category')
df['status'] = df['status'].cat.codes

labels = df['status']
data = df.iloc[:, :-1]

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
clf.score(X_test, y_test) 

