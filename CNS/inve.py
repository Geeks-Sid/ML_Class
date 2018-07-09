
def funcs(x, y, z):
	m = z
	a = x
	b = y
	rem = -1
	while(rem!=1):
		temp1 = m
		temp2 = a
		quot = m//a
		rem = m%a
		print(m,"=", a, "(", quot, ") + ", rem)
		m = a
		a = rem
	return -(temp1//temp2)
def GCD(x, y):

   while(y):
       x, y = y, x % y

   return x

print("Enter the values of a, b, m for the equation ax ~ b mod m :")
a = int(input())
b = int(input())
m = int(input())
print("Typed EQUATION : ",a,"x ~",b,"mod",m)

t = GCD(a, b)
a /= t
b /= t
temp_m = m
m /= t
inv = funcs(a, b, m)
print("inverse is: ", inv)
for i in range(3):
	print("\n")
	x = inv * (b + (m*i)) 
	for i in range(-5, 5):
		print(int(x + (i * temp_m)), end = ",")

print("\n")
