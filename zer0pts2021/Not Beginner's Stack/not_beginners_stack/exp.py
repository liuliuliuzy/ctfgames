# from pwn import *
# s = remote('pwn.ctf.zer0pts.com', 9011)
# s.interactive()

import pwn

if pwn.args.YES:
    print("yes")
else:
    print("no")