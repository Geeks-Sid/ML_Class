import math

def get_factors(n):
    factors = {}
    i = 2
    while i<n+1:
        print(i)
        if n%i == 0:
            key = str(i)
            if key in factors:
                factors[key] += 1
            else:
                factors[key] = 1
            n = n/i
            print("Value of n: ",n)
        else:
            i+=1
    return factors

print("Enter the values of a, b and c in the form of a^b mod c: ")
a = int(input())
b = int(input())
c = int(input())

phi = c
x = get_factors(c)
for key in x:
    print(key, x[key])
    t = float((1 - (1/int(key))))
    print("T",t)
    phi = phi * t
print(phi)
phi = int(phi)
rem = b % phi
div = b // phi
print("(",a,"^", phi,"(", div, ")", ".", a,"^", rem, "%", "", b)
print("Final = ", a, "^", rem, " = mod", c)
print("Ans =", (a ** rem)%c)

