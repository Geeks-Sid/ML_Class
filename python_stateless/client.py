import socket               
 
s = socket.socket()         
import time
 
port = 12345               

s.connect(('127.0.0.1', port))

print 'Socket Connected to ' + '127.0.0.1' + ' on ip ' + str(port)
num = input("Please enter a number of your choice")
s.send(str(num))
print s.recv(1024)
print s.recv(1024)
print('message received')
s.close()       