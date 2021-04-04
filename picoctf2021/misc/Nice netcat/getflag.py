from pwn import *

p = remote('mercury.picoctf.net', 43239)

x = b' '
flag = ''
while x:
    x = p.recvline()
    # print(x)
    flag += chr(int(x[:-2].decode(), 10))
    print(flag)
