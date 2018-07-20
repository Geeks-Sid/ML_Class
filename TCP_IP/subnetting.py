import numpy as np
import time

def get_n(num):
    n = 0
    while(True):
        if 2**n >= num:
            break
        else:
            n += 1
    return n

def ip_print(arr):
    c = ""
    for i in range(len(arr)):
        c = c + str(arr[i])
        c = c + '.'
    return c

def get_subnet(ip, los, nos, calc_snets, ip_class):
    if nos == calc_snets:
        t = 2**(32-los)
        print("\mNumber of ip per subnet :", t)
        print("first 3 ip subnets look like", ip, los, nos, calc_snets, ip_class)
        num_ip_p =  int(input("How many first and last IPs would you like to look at?"))
        maxm = 256
        if t <= maxm:
            var = int(maxm/t)
            if ip_class == 'B':
                x = ip.strip().split(".")
                x = [int(i) for i in x]
                for i in range(num_ip_p):
                    for i in range(var):
                        print(ip_print(x), "--",ip_print([x[0], x[1], x[2], x[3]+t-1]))
                        if x[3]+t >= maxm:
                            x[3] = 0
                            x[2] += 1
                        else: 
                            x[3] += t
        else:
            t /= 256
            t = int(t)
            var = int(maxm/t)
            if ip_class == 'B':
                x = ip.strip().split(".")
                x = [int(i) for i in x]
                for i in range(num_ip_p):
                    print("this is ", x)
                    time.sleep(2)
                    if x[3]+256-1 >= maxm:
                        x[3] = 0
                        x[2] += t
                    print(ip_print(x), "--",ip_print([x[0], x[1], x[2]+t-1, x[3]+256-1]))
                    x[3] += 256-1
        print("-----------------------------------------------")
        print("The last 3 subnets look like : ")
        
    else:
        t = 2**(32-los)
        print("\mNumber of ip per subnet :", t)
        print("first 3 ip subnets look like", ip, los, nos, calc_snets, ip_class)
        num_ip_p =  int(input("How many first and last IPs would you like to look at?"))
        maxm = 256
        if t <= maxm:
            var = int(maxm/t)
            if ip_class == 'B':
                x = ip.strip().split(".")
                x = [int(i) for i in x]
                for i in range(num_ip_p):
                    for i in range(var):
                        print(ip_print(x), "--",ip_print([x[0], x[1], x[2], x[3]+t-1]))
                        if x[3]+t >= maxm:
                            x[3] = 0
                            x[2] += 1
                        else: 
                            x[3] += t
        else:
            t /= 256
            t = int(t)
            var = int(maxm/t)
            if ip_class == 'B':
                x = ip.strip().split(".")
                x = [int(i) for i in x]
                for i in range(num_ip_p):
                    print("this is ", x)
                    time.sleep(2)
                    if x[3]+256-1 >= maxm:
                        x[3] = 0
                        x[2] += t
                    print(ip_print(x), "--",ip_print([x[0], x[1], x[2]+t-1, x[3]+256-1]))
                    x[3] += 256-1
        print("-----------------------------------------------")
        print("The last 3 subnets look like : ")
        x = (nos * t)/256
        print("First 3 ip subnets look like : ")
    return
         
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
        if los  <= 32:
            print("Length of subnet mask :", los)
            print("Number of ips per subnet:", 2**(32-los))
            print("Subnet Mask:", end = "")
            temp = los
            for i in range(4):
                if temp - 8 >= 0:
                    x = 8                    
                    temp -= 8
                    print(2**x-1, end=".")
                elif temp > 0:
                    x = 8 - temp
                    temp -= temp
                    print(2**x, end=".")
                else:
                    x = 0
                    print(2**x-1, end=".")
            c = get_subnet(ip, los, nos, calc_snets, 'B')
        else:
            print("Sorry, too many subnets to divide! This class cant hold that much.")            
        
    elif x[0] < 224:
        print("Your ip address ", ip, "Belongs to class C")
        print("Net id:", x[0], "\b.", x[1], "\b.", x[2], "\b.0")
        print("Host id:", x[3])
        los = 24+n
        if los <=32:
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
        else:
            print("Sorry, too many subnets to divide! This class cant hold that much.")            

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
