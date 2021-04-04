from pwn import *
import sys
# context.log_level = "debug"

p = remote("mercury.picoctf.net", 64260)

encflag = bytes.fromhex('51466d4e5f575538195551416e4f5300413f1b5008684d5504384157046e4959')

print(len(p.recv()))
# payload = b'a'*(50000-32)+encflag
payload = b'a'*968
p.sendlineafter("encrypt? ", payload)
p.recvuntil("go!\n")
content = p.recv()
# p.success("length: {:d}".format(len(content)))
# p.success(content.decode())
# 1000*49
for i in range(49):
    p.success("{}th round".format(i+1))
    payload = b"a"*1000
    p.sendlineafter("encrypt? ", payload)
    p.recvuntil("go!\n")
    p.recv()

payload = encflag
p.sendlineafter("encrypt? ", payload)
p.recvuntil("go!\n")
x = p.recv()

p.success("flag: picoCTF{{{}}}".format(bytes.fromhex(x[:64].decode()).decode()))

# x = '3361313639343464616434333237313763636333393435643364393634323161'
# print(bytes.fromhex(x))
# flag: picoCTF{3a16944dad432717ccc3945d3d96421a}