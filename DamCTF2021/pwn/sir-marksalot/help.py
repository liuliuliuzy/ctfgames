# flag = True
# for i in range(39):
#     for j in range(39):
#         command = b''
#         if flag:
#             command = b'a'
#         else:
#             command = b'd'
#         try:
#             # p.sendlineafter(b'm - show map): ', b'x')
#             # p.sendlineafter(b'What would you like to write?\n', move_all_payload)
#             # p.sendlineafter(b'm - show map): ', command) # move left or right
#             print(command.decode()+str(j), end=' ')
#         except:
#             p.interactive()
#     try:
#         # p.sendlineafter(b'm - show map): ', b'w') # move up
#         print('w')
#     except:
#         p.interactive()
#     flag = not flag

x = 1

def change():
    global x
    x -= 1

print(x)
change()
print(x)