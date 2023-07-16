#!/usr/bin/python

li = []
for i in range(65,91):
    li.append(chr(i))
for i in range(10):
    li.append(str(i))
li.append('_')
enc= open('message.txt','r')
e = (enc.read()).split(' ')[:-1]
flag =''
for i in range(len(e)):
    flag+=li[(int(e[i]) % 37)]
print(flag)

