#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:23:44 2018

@author: dalab
"""

#ip = input("Enter the IP Packet :")
ip = 'ac100a63ac100a0c'
x = list(ip)

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
