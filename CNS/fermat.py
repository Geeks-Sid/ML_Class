import math

def check_prime(n):
    flag = True
    for i in range(2, math.sqrt(n)):
        if n%i == 0:
            flag = False
    return flag

def get_mod(x, y):
    return x%y

print("*******************")
print("* a^x = b mod c  *")
print("*******************")
a = int(input("Enter the base number a :"))
x = int(input("Enter the base number x :"))
b = int(input("Enter the base number b :"))
c = int(input("Enter the base number c :"))

if not check_prime(c):
    print("Sorry, C is not prime, please enter a prime number")
    exit()

def get_closest(x, c):
    _temp = c-1
    num = x // _temp
    
    return
