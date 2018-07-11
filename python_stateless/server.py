import socket               
import os
s = socket.socket()         
print "Socket successfully created"
 
port = 12345               
 
s.bind(('', port))        
print "socket binded to %s" %(port)
 
s.listen(5)     
print "socket is listening"           

def comp_cube(n):
    return n**3
while True:
 
   c, addr = s.accept()    
   print 'value of c is', c
   print 'Got connection from', addr
   if os.path.exists(os.path.join('/home/cnlab-10/Documents/server_logs',addr[0] + '.txt')):
       c.send('Hello, you are a old user')
   else:
       c.send('Hello, you are a new client')
       open(os.path.join('/home/cnlab-10/Documents/server_logs',addr[0] + '.txt'), 'a').close()
   data = c.recv(1024)
   data = int(data)
   data = comp_cube(data)
   data = str(data)
   c.send('The cube of number is:')
   c.send(data)
#   c.send(cube)
   c.send('\nThank you for connecting')
 
   c.close()