#!usr/bin/python

flag_hex= '7069636f4354467b41534349495f49535f454153595f38393630463041467d'

flag = bytes.fromhex(flag_hex).decode("utf-8")
print(flag)
