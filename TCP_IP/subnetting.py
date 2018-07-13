import numpy as np

def get_n(num):
    n = 0
    while(True):
        if 2**n >= num:
            break
        else:
            n += 1
    return n
            
import sys
while(True):
    ip = input("Enter the IP address in dotted decimal format: ")
    x = ip.strip().split(".")
    x = [int(i) for i in x]
    for i in range(4):
        if x[i]>255 or x[i] < 0 or len(x) < 4 or len(x) > 4:
            print("You entered wrong ip address")
            sys.exit()
            break
    nos = int(input("Please enter the number of subnets(try 2^n):"))
    i = 0
    n = get_n(nos)
    calc_snets = 2**n
    print("You selected ", nos, "number of subnets and we are choosing ", calc_snets)
    
    if x[0] < 128:
        print("Your ip address ", ip, "Belongs to class A")
        print("Net id:", x[0], "\b.0.0.0")
        print("Host id:", x[1], "\b.",x[2], "\b.", x[3])
        los = 8+n
        print("Length of subnet mask :", los)
        print("Number of subnets :", 2**(32-los))
    elif x[0] < 192:
        print("Your ip address ", ip, "Belongs to class B")
        print("Net id:", x[0], "\b.", x[1], "\b.0.0")
        print("Host id:", x[2], "\b.", x[3])
        los = 16+n
        print("Length of subnet mask :", los)
        print("Number of subnets :", 2**(32-los))
        print("Subnet Mask:", end = "")
        temp = los
        for i in range(4):
            if temp - 8 >= 0:
                x = 8
            elif temp > 0:
                x = temp
            else:
                x = 0
            print(2**x-1, end=".")
            
        
    elif x[0] < 224:
        print("Your ip address ", ip, "Belongs to class C")
        print("Net id:", x[0], "\b.", x[1], "\b.", x[2], "\b.0")
        print("Host id:", x[3])
        los = 24+n
        print("Length of subnet mask :", los)
        print("Number of subnets :", 2**(32-los))
        print("Subnet Mask:", end = "")
        temp = los
        for i in range(4):
            if temp - 8 >= 0:
                temp -= 8
                x = 8
            elif temp > 0:
                temp -= temp
                x = temp
            else:
                x = 0
            print(2**x-1, end=".")

    elif x[0] < 240:
        print("Your ip address ", ip, "Belongs to class D")
        print("Net id:", x[0], "\b.", x[1], "\b.", x[2], "\b.0")
        print("Host id:", x[3])
        los = 24+n
        print("Length of subnet mask :", los)
        print("Number of subnets :", 2**(32-los))
    else:
        print("Your ip address ", ip, "Belongs to class E")
        print("Net id:", x[0], "\b.", x[1], "\b.", x[2], "\b.0")
        print("Host id:", x[3])
        los = 24+n
        print("Length of subnet mask :", los)
        print("Number of subnets :", 2**(32-los))