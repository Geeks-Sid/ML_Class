import numpy as np
import math
def upt(ip):
    print("The value after unipolar threshold activation is: ", 1 if ip>0 else 0)

def bpt(ip):
    print("The value after bipolar threshold activation is: ", 1 if ip>0 else -1)
    
def ups(ip):
    print("Enter the steepness factor lambda:")
    lamb = float(input())
    print("The value after unipolar threshold activation is: ", (1/(1+(math.e**(-lamb*net)))) if ip>0 else 0)

def bps(ip):
    print("Enter the steepness factor lambda:")
    lamb = float(input())
    print("The value after unipolar threshold activation is: ", ((1-(math.e**(-lamb*net)))/(1+(math.e**(-lamb*net)))) if ip>0 else 0)

n = int(input("Enter the number of features:"))
x = np.zeros(n)
w = np.zeros(n)
print("Enter the features:")
for i in range(n):
    x[i] = int(input())

print("Enter the weights:")
for i in range(n):
    w[i] = int(input())

net = np.matmul(w, x)
print("Calculated net:", net)
print("Please select an activation function -")
print("1.Unipolar Threshold\n2.Bipolar Threhold")
print("3.Unipolar Sigmoid\n4.Bipolar Sigmoid\n5.All activation")

print("Enter the choice of activation function")
c = int(input())
if c == 1:
    upt(net)
elif c == 2:
    bpt(net)
elif c == 3:
    ups(net)
elif c == 4:
    bps(net)
elif c == 5:
    upt(net)
    bpt(net)
    ups(net)
    bps(net)
else :
    print("Sorry, wrong choice of activation")