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
    if x[0] < 128:
        print("Your ip address ", ip, "Belongs to class A")
        print("Net id:", x[0], "\b.0.0.0")
        print("Host id:", x[1], "\b.",x[2], "\b.", x[3])
    elif x[0] < 192:
        print("Your ip address ", ip, "Belongs to class B")
        print("Net id:", x[0], "\b.", x[1], "\b.0.0")
        print("Host id:", x[2], "\b.", x[3])
    elif x[0] < 224:
        print("Your ip address ", ip, "Belongs to class C")
        print("Net id:", x[0], "\b.", x[1], "\b.", x[2], "\b.0")
        print("Host id:", x[3])
    elif x[0] < 240:
        print("Your ip address ", ip, "Belongs to class D")
        print("Net id:", x[0], "\b.", x[1], "\b.", x[2], "\b.0")
        print("Host id:", x[3])
    else:
        print("Your ip address ", ip, "Belongs to class E")
        print("Net id:", x[0], "\b.", x[1], "\b.", x[2], "\b.0")
        print("Host id:", x[3])
