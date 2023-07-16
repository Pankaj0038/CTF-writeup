#!/usr/bin/python
user = open('usernames.txt','r')
pas = open('passwords.txt','r')
usr = user.readlines()
password = pas.readlines()
def ind(args):
    for index,line in enumerate(usr):
        if str(line.strip()) == 'cultiris':
            return index
index = ind(usr)
print(index)
print(password[index])
