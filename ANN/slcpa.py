import numpy as np
import matplotlib.pyplot as plt

def get_net(w, x):
	return np.matmul(w, x)

def get_act(v):
	return (1-np.e**(-v))/(1+np.e**(-v))
	
def adjust_positive(weight, y, eta, ao, do):
	adjusted_weight = weight + 0.5*eta*y*(do-ao)*(1-(ao**2))
	print (adjusted_weight, weight, y)
	return adjusted_weight

def get_err(ao, do):
	if ao != do:
		return 0.5*((ao-do)**2)
	
emax = 0.001
#data_labels = np.array([-1, 1, 1, 1])
#data_labels = np.array([-1, -1, -1, 1])
data_labels = np.array([-1, 1, 1, -1])
print ('data_labels = ', data_labels)

print ("Enter the learning rate(default = 1):")
eta = int(input())

new_data_points = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
print ("Enter the initial weight matrix(3 values):")
w = np.zeros(3)
for i in range(3):
	print ("Enter the value of w", i)
	w[i] = float(input())
	
P = 4
k = 1
cycle = 1

while(True):
	ERROR = 0
	print ('---------------------------------------------------')
	print ("Current cycle:", cycle)
	print ('---------------------------------------------------')
	for p in range(P):
		print ('value of p', p+1)
		print ('current_weights', w)
		print ('current_points', new_data_points[p])
		print ('current_label', data_labels[p])
		net = get_net(w, new_data_points[p])
		print (k, 'net = ', net)
		act = get_act(net)
		print (k, 'act = ', act)
		w = adjust_positive(w, new_data_points[p], eta, act, data_labels[p])
		print ('iteration ', k, 'weights_adjusted')
		ERROR += get_err(act, data_labels[p])
		print ('Current_adjust_weights:', w)
		print ('Current_error:', ERROR)
		print ('--------------------------------------------------------')
		k+=1
	print ("Cycle error:", ERROR)
	cycle+= 1
	if ERROR < emax:
		break

plt.scatter(1, 0, marker = 'x')
plt.scatter(1, 1, marker = 'x')
plt.scatter(0, 1, marker = 'x')
plt.scatter(0, 0, marker = 'o')
plt.plot([0, 1/2], [1/2, 0])
