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
            
x = get_factors(60)

phi = 60
for key in x:
    print(key, x[key])
    t = float((1 - (1/int(key))))
    print("T",t)
    phi = phi * t
    print(phi)