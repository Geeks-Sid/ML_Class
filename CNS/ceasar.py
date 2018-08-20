import numpy as np

class ceasar_cipher():
    def __init__(self):
        pass
    
    def encrypt(self, msg, key):
#        print("Inside encrypt")
        x = list(msg)
#        print("Breaking message:", x)
        y = [self.__convert_char(i) for i in x]
#        print("Converted to int:", y)
        y = [(i + key)%26 for i in y]
#        print("Key added:", y)
        enc = [self.__convert_num(i) for i in y]
#        print("Message Encrypted", enc)
        return ''.join(enc)    
    
    def decrypt(self, msg, key):
#        print("Inside decrypt")
        x = list(msg)
#        print("Breaking message:", x)
        y = [self.__convert_char(i) for i in x]
#        print("Converted to int:", y)
        y = [(i - key)%26 for i in y]
#        print("Key subtracted:", y)
        dec = [self.__convert_num(i) for i in y]
#        print("Message decrypted", dec)
        return ''.join(dec)
    
    def __convert_num(self, num):
        if num + 64 <= 90:
            return chr(num+64)
        else :
            return 'X'
        
    def __convert_char(self, old):
        if len(old) != 1:
            return 0
        new = ord(old)
        if 65 <= new <= 90:
            return new - 64
        elif 97 <= new <= 122:
            return new - 96
        return 0
    
c = ceasar_cipher()
message = 'SIDDHESH'
print('Message', message)
encrypted_message = c.encrypt('SIDDHESH', 16)
print("Encrypted message", encrypted_message)
decrypted_message = c.decrypt(encrypted_message, 16)
print("Decrypted message", decrypted_message)
