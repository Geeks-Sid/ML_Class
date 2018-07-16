import numpy as np

def sumn(a, p, s):
    prd = 0
    for i in range(a.shape[0]):
        prd += a[i] * p[i] * s[i]
    return prd

def modInverse(c, d) :
    c = c % d;
    for x in range(1, d) :
        if ((c * x) % d == 1) :
            return x
    return 1
 
n = int(input("Enter the number of equations:"))

a = np.zeros(n, dtype = np.int16)
m = np.zeros(n, dtype = np.int16)
s = np.zeros(n, dtype = np.int16)

for i in range(n):
    print("Enter the values of a, m for eqn", i+1, "one after the other:")
    a[i] = int(input())
    m[i] = int(input())

p = np.zeros(n)
print "P is initialized", p.shape
mpr = 1

for i in range(n):
    mpr *= m[i]

for i in range(n):
    p[i] = mpr/m[i]
    print "p[",i+1,"]=",p[i]

for i in range(n):
    s[i] = modInverse(p[i], m[i])
    print "s[",i+1,"]=",s[i]
    
sumn = sumn(a, p, s)
x = sumn
while(x<0):
    x += mpr
while(x>0):
    x-=mpr
while(x<0):
    x += mpr

print("Solution: ", x)
