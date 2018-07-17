import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
column = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'status']
df = pd.read_csv('/home/cnlab-14/Documents/DTC/car.data', header = None)
df.columns = column
import math

labels = df['status']
data = df.iloc[:, :-1]

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)

count_unacc = df[df['status'] == 'unacc'].count()
count_acc = df[df['status'] == 'acc'].count()
count_good = df[df['status'] == 'good'].count()
count_vgood = df[df['status'] == 'vgood'].count()

counts = {'unacc':count_unacc[0], 'acc':count_acc[0], 'good':count_good[0],
          'vgood':count_vgood[0]}
def entropy():
    return

def get_col_entropy():
    return

def get_mul_log(n, k):
    return -(n/k)*(math.log2(n/k))

def tot_entropy(counts_dict):
    x = 0
    tot_count = sum(counts_dict.values())
    for key in counts_dict:
        x += get_mul_log(counts_dict[key], tot_count)
    return x

tot_entropy_val = tot_entropy(counts)

m = {}
for c in column:
    for key in counts:
        x = df[df[c] == key].count()
        m[key+'_'+c] = x[0]
        print(c)
def gain(some_list):
    yy
    

#
#df[(df['persons'] == '2') & (df['status'] == 'unacc')].count()
#df[df['persons'] == '2'].count()
#df[df['status'] == 'unacc'].count()
