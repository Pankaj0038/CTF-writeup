#!usr/bin/python
import string
enc = str(input("enter the encoded flag: "))
alpha = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord ('a')
def b16_decode(enc):
    enc2 = ""
    for i in range(0,len(enc),2):
        a = "{0:04b}".format((ord(enc[i])-97))
        b = "{0:04b}".format(ord(enc[i+1])-97)
        enc2 += chr(int((a+ b),2))
    #print("partial flag: ",enc2,end='')
    return enc2
encoded = b16_decode(enc)

def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return alpha[(t1 + t2) % len(alpha)]

for key in alpha:
    flag = ''
    print(key)
    for c in enc:
        flag += shift(c,key)
    print('flag',b16_decode(flag),end = "\n") 
