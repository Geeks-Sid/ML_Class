def power(x, y, p):
    res = 1
    x = x%p
    
    while(y>0):
        if y%2 == 1:
            res = (res * x) % p
        y = y // 2
        x = (x**2) %p
    return res

def modInverse(a, p):
    return power(a, p-2, p)

def modFact(n, p):
    if p <= n:
        return 0
    
    res = p-1
    for i in range(n+1, p):
        res = (res * modInverse(i, p))%p
    return res

n = 25
p = 29
print("Final:" , modFact(n, p))