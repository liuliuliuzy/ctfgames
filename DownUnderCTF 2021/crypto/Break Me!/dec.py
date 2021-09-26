from pwn import *
from base64 import b64decode, b64encode
import string
# context.log_level = 'debug'
p = remote('pwn-2021.duc.tf', 31914)

# for i in range(1,18):
#     payload = b'a'*i
#     p.sendlineafter(b'Enter plaintext:\n', payload)
#     rec = b64decode(p.recvline().decode())
#     print(len(rec), payload)
payload = b'a'
p.sendlineafter(b'Enter plaintext:\n', payload)
enc_flag = b64decode(p.recvline().decode())[:32]
# print(flag)

flag_len = 32 # bytes
key_len = 16 # bytes
payload = b'a'*16
key = '!_SECRETSOURCE_!'
# for i in range(16):
#     for x in string.printable:
#         # print("try", i, x)
#         payload = x.encode() + key.encode() + b'0'*16
#         print(payload)
#         p.sendlineafter(b'Enter plaintext:\n', payload)
#         rec = b64decode(p.recvline().decode())
#         # print(payload, s)
#         # print(payload, rec[32:48], rec[64:], sep='\n')
#         if rec[32:48] == rec[64:]:
#             key = x + key
#             print(key)
#             break
from Crypto.Cipher import AES

cipher = AES.new(key.encode(), AES.MODE_ECB)
flag = cipher.decrypt(enc_flag)
print(flag)
# DUCTF{ECB_M0DE_K3YP4D_D474_L34k}

# payload = b'"' + b'0'*16
# p.sendlineafter(b'Enter plaintext:\n', payload)
# rec = b64decode(p.recvline().decode())
# print(rec[:32], rec[32:48], rec[48:64], rec[64:], sep='\n')
# print(key)

p.interactive()