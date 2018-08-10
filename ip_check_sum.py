import numpy as np
#ip = '45000078 00650000 08110000 ac100a63 ac100a0c'
ip = '450000780065000008110000c910200dd7041014'

x = list(ip)

def ip_printer(my_temp_ip):
    ip_to_print = []
    for i in range(0, 8, 2):
        temp = my_temp_ip[i] + my_temp_ip[i+1]
        ip_to_print.append(int(temp, 16))
    print(*ip_to_print, sep = '.')   
    return ip_to_print

def get_version(x):
    return int(x[0], 16)

def get_header_length(x):
    return int(x[1], 16)

def get_service_type(x):
    temp = x[2] + x[3]
    print(temp)
    return int(temp, 16)

def get_total_length(x):
    temp = ''.join(x[4:8])
    return int(temp, 16)

def get_identification(x):
    temp = ''.join(x[8:12])
    return int(temp, 16)

def get_flags(x):
    temp = ''.join(x[12:16])
    temp = int(temp, 16)
    temp = np.binary_repr(temp, 16)
    return temp[:3]

def get_frag_bits(x):
    temp = ''.join(x[12:16])
    temp = int(temp, 16)
    temp = np.binary_repr(temp, 16)
    return temp[3:16]

def get_ttl(x):
    temp = x[16] + x[17]
    return int(temp, 16)

def get_protocol(x):
    temp = x[18] + x[19]
    temp = int(temp, 16)
    if temp == 17:
        return 'UDP'
    elif temp == 6:
        return 'TCP'
    else:
        return temp
    
def get_checksum(x):
    temp = ''.join(x[20:24])
    return temp

def get_source_ip(x):
    SIP = x[24:32]
    SIP = ''.join(SIP)
    SIP = ip_printer(SIP)
    return SIP
    
def get_destination_ip(x):
    DIP = x[32:40]
    DIP = ''.join(DIP)
    DIP = ip_printer(DIP)
    return DIP
        
def calculate_check_sum(x):
    CSUM = int('0000', 16)
    for i in range(0, 40, 4):
        t = x[i] + x[i+1] + x[i+2] + x[i+3]
        t = int(t, 16)
        if (CSUM + t) // 65536 > 0:
            val = (CSUM + t) // 65536
            CSUM = CSUM + t
            CSUM = CSUM % 65536
            CSUM += val
        else:
            CSUM += t
    return hex(CSUM)[2:]
        
def replace_in_packet(x, check_sum):
    x[20:24] = check_sum
    return ''.join(x)

def verify_new_packet():
    pass


SIP = x[-16:-8]
SIP = ''.join(SIP)

DIP = x[-8:]
DIP = ''.join(DIP)

NEW_SIP = [SIP[i] + SIP[i+1] + SIP[i+2] + SIP[i+3] for i in range(0, 8, 4)]
NEW_DIP = [DIP[i] + DIP[i+1] + DIP[i+2] + DIP[i+3] for i in range(0, 8, 4)]

print("Source IP:", NEW_SIP)
print("Destination IP:", NEW_DIP)

print("============CHECKING============")
CSUM = int('0000', 16)
for i in range(2):
    t = int(NEW_SIP[i], 16)
    CSUM += t
for i in range(2):
    t = int(NEW_DIP[i], 16)
    CSUM += t
print('CSUM', hex(CSUM%65536 + CSUM//65536))              
t = CSUM%65536 + CSUM//65536
CSUM = t
new_csum = int('ffff', 16) - CSUM 
new_csum += 1   
print('HEX CSUM = ', hex(new_csum)) 
print(65536 - (CSUM+new_csum))    
print('=========CREATING NEW PACKET===========')
ip = ip + hex(new_csum)[2:]

print('=========CHECKING NEW IP PACKET ==========')
x = list(ip)
SIP = x[-20:-12]
SIP = ''.join(SIP)
DIP = x[-12:-4]
DIP = ''.join(DIP)
CSUM = x[-4:]
t = int('0000', 16)
for i in range(0, 20, 4):
    t += int(''.join(x[i:i+4]), 16)
t = (t%65536 + t//65536)
if t%65536 == 0:
    print("THE NEW IP PACKET WAS NOT DAMAGED")
else:
print("THE NEW IP PACKET WAS DAMAGED")
