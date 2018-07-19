import numpy as np
import matplotlib.pyplot as plt

def get_net(w, x):
	return np.matmul(w, x)

def get_act(v):
	if v>0:
		return 1
	else:
		return -1

def adjust_positive(weight, y):
	adjusted_weight = weight + y
	print(adjusted_weight, weight, y)
	return adjusted_weight
	
def adjust_negative(weight, y):
	adjusted_weight = weight - y
	print(adjusted_weight, weight, y)
	return adjusted_weight

def get_err(ao, do):
	if ao != do:
		return 2
	else:
		return 0	
	
data_points = np.array(([[4, 4, 1], [3, 4, 1], [4, -3, 1], [4, -4, 1], [-3, -3, 1], [-4, -3, 1]]))
data_labels = np.array(([[1, -1, -1], [1, -1, -1], [-1, 1, -1], [-1, 1, -1], [-1, -1, 1], [-1, -1, 1]]))

plt.scatter(data_points[0][0], data_points[0][1], marker = 'o')
plt.scatter(data_points[1][0], data_points[1][1], marker = 'o')
plt.scatter(data_points[2][0], data_points[2][1], marker = 'x')
plt.scatter(data_points[3][0], data_points[3][1], marker = 'x')
plt.scatter(data_points[4][0], data_points[4][1], marker = 'v')
plt.scatter(data_points[5][0], data_points[5][1], marker = 'v')  

for i in range(6):
    print("y", i+1, " = ", data_points[i])
    print("d", i+1, " = ", data_labels[i])

w  = np.array([[-1, -1, -1], [-2, -2, -2], [-3, -3, -3]])
print("Initialized weight matrix is = ")
for i in range(3):
    print(w[i])
print("Enter the learning rate(default = 1):")
c = int(input())


print "Enter the initial weight matrix(3 values):"
w = np.zeros(3)
for i in range(3):
	print "Enter the value of w", i 
	w[i] = float(input())
	
P = 4
k = 1
cycle = 1

while(True):
	ERROR = 0
	print '---------------------------------------------------'
	print "Current cycle:", cycle
	print '---------------------------------------------------'
	for p in range(P):
		print 'value of p', p+1
		print 'current_weights', w
		print 'current_points', new_data_points[p]
		print 'current_label', data_labels[p]
		net = get_net(w, new_data_points[p])
		print k, 'net = ', net
		if net == 0:
			act = data_labels[p] * -1
		else:
			act = get_act(net)
		print k, 'act = ', act
		if act == data_labels[p]:
			print 'iteration ', k, 'weights_not adjusted'
		else:	
			if data_labels[p] == 1:
				w = adjust_positive(w, new_data_points[p])
			else:
				w = adjust_negative(w, new_data_points[p])
			print 'iteration ', k, 'weights_adjusted' 
		ERROR += get_err(act, data_labels[p])
		print 'Current_adjust_weights:', w
		print 'Current_error:', ERROR
		print '--------------------------------------------------------'
		k+=1
	print "Cycle error:", ERROR
	cycle+= 1
	if ERROR == 0:
		break
"""

