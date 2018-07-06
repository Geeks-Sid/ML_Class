import numpy as np
print("Please enter your IP address:")
ip = input()
c = ip.split(".")
arr = np.zeros(4)

for i in range(len(c)):
    if c[i].startswith('0') and int(c[i])!=0:
        print("***********WARNING***********")
        print(c[i], "strted with '0', next time please avoid starting with '0'. We converted it for now, don't worry.")
    arr[i] = int(c[i])
for i in range(4): 
    if arr[i] > 255 or arr[i] < 0:
        print("Please enter values between 0-255 only.")
        choice = '0'
        while(choice!='Y' and choice!='y' and choice!='N' and choice!='n'):
            print("Wrong choice! Please try again.")
            print("Do you wish to correct this number ",arr[i],"?(Y/N)")
            choice = input()
            print(choice=='Y')
            print(choice!='Y' or choice!='y' or choice!='N' or choice!='n')
        if choice == 'Y' or choice == 'y':
            print("Please enter the corrected value")
            arr[i] = input("Enter now:")
        elif choice!='N' or choice!='n': 
            print("Okay, restarting the process now. Good bye")
            break
arr = np.array(arr, dtype = np.uint8)
c = []
print("Array before binary:", arr)
for i in range(4):
    print(arr[i])
    c.append(np.binary_repr(arr[i], width = 8))          
print("Dotted binary_representation is:")
for i in range(4):
    print(c[i], end='.')
print("\n")
