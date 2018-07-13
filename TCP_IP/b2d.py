import numpy as np

#def arr_to_dec(arr):
#    sum = 0
#    for i in range(8):
#        sum += arr[i] * (2**i)
#    return sum
#    
#x1 = str(input("Enter the first octet:"))
#x2 = str(input("Enter the second octet:"))
#x3 = str(input("Enter the third octet:"))
#x4 = str(input("Enter the fourth octet:"))
#x = [i for i in x1]
#x = [int(i) for i in x]
#y = [i for i in x2]
#y = [int(i) for i in y]
#z = [i for i in x3]
#z = [int(i) for i in z]
#a = [i for i in x4]
#a = [int(i) for i in a]
#if len(x) < 8:
#    print("Sorry, we you entered a smaller first octet, we are padding it with zeros")
#elif len(x) > 8:
#    print("Sorry, you entered a value larger than 255, please try again")    

arr = []
ip = np.zeros((4, 8))
i = 0
while(i!=4):
    print("Enter the ",i+1, " octet:")
    t = input()
    if len(t) > 8 or len(t) < 8:    
        print("Sorry! Please try again. Please enter values between 0-255 only")
    else:
        x = int(t, 2)
        arr.append(x)
        i+=1

print("Your decimal ip is:")
for i in range(4):
    print(arr[i], end = ".")
