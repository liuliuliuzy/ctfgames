from pwn import *

s = remote("52.149.135.130", 4869)

s.recvuntil('flag : ')
enc_flag_hex_str = s.recv(160)

candis = [[bytes([i]) for i in range(256)] for j in range(32)]
# print(candis)
key = b''*32

while len(candis[0]) > 1:
    s.recvuntil(b'> ')
    s.sendline(b'1')
    c = s.recvline()
    if b'Something seems leaked !' in c:
        continue
    if bytes.fromhex(c[:2].decode()) in candis[0]:
        candis[0].remove(bytes.fromhex(c[:2].decode()))
        print(len(candis[0]), ": ", bytes.fromhex(c[:2].decode()))

print(candis[0])


s.interactive()
