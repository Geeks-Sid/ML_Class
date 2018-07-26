import numpy as np
import matplotlib.pyplot as plt
#%%	
y = np.array(([[4, 4, 1], [3, 4, 1], [4, -3, 1], [4, -4, 1], [-3, -3, 1], [-4, -3, 1]]))
d = np.array(([[1, -1, -1], [1, -1, -1], [-1, 1, -1], [-1, 1, -1], [-1, -1, 1], [-1, -1, 1]]))
#y = np.array(([[10, -2, -1], [2, -5, -1], [-5, 5, -1]]))
#d = np.array(([[1, -1, -1], [-1, 1, -1], [-1, -1, 1]]))
o = np.empty((3, 1))
plt.scatter(y[0][0], y[0][1], marker = 'o', color = 'r')
plt.scatter(y[1][0], y[1][1], marker = 'o', color = 'R')
plt.scatter(y[2][0], y[2][1], marker = 'x', color = 'b')
plt.scatter(y[3][0], y[3][1], marker = 'x', color = 'b')
plt.scatter(y[4][0], y[4][1], marker = 'v', color = 'g')
plt.scatter(y[5][0], y[5][1], marker = 'v', color = 'g')  
#%%
for i in range(y.shape[0]):
    print("y", i+1, " = ", y[i])
    print("d", i+1, " = ", d[i])

w  = np.array([[-1, -1, -1], [-2, -2, -2], [-3, -3, -3]])
print("Initialized weight matrix is = ")
for i in range(3):
    print(w[i])

c = 1
train_cycles = 0

#%%
print("Training begins")
P = 6
k = 1
cycle = 1
flag = False
while not flag:
    train_cycles = train_cycles + 1
    ERROR = 0
    for p in range(y.shape[0]):
        k = k + 1
        for i in range(w.shape[0]):
            neti = np.matmul(np.transpose(w[i]), y[p])
            if neti < 0:
                o[i] = -1
            elif neti > 0:
                o[i] = 1
            else:
                o[i] = -d[p][i]
            w[i] = w[i] + int(((c * (d[p][i] - o[i])) / 2)) * y[p]
            ERROR = ERROR + int((((d[p][i] - o[i]) ** 2) / 2))
    if ERROR == 0:
        flag = True
        print("Training Cycles=", train_cycles)
        print("Steps=", k)
        print("Final weight matrix W=\n", w)
        print("ERROR =", ERROR)

#%%
def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')
plt.scatter(y[0][0], y[0][1], marker = 'o', color = 'r')
plt.scatter(y[1][0], y[1][1], marker = 'o', color = 'R')
plt.scatter(y[2][0], y[2][1], marker = 'x', color = 'b')
plt.scatter(y[3][0], y[3][1], marker = 'x', color = 'b')
plt.scatter(y[4][0], y[4][1], marker = 'v', color = 'g')
plt.scatter(y[5][0], y[5][1], marker = 'v', color = 'g')  
for i in range(3):
    abline(w[i][1]/ w[i][0], w[i][2])
