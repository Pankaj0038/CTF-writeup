#!usr/bin/python

enc = open("enc.txt").read()
def enc2hex(enc):
	flag=''
	for char in enc:
    		flag += hex(ord(char)).lstrip("0x")
	return flag

flag = enc2hex(enc)
final = bytes.fromhex(flag).decode("utf-8")
print(final)
