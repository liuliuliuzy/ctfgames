
# flag = "picoCTF{this_is_a_flaga}"

# res = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# flagx = "E781A9E68DAFE48D94E499BBE384B6E5BDA2E6A5B4E78D9FE6A5AEE78DB4E38CB4E6919FE6BDA6E5BCB8E5BCB0E391A3E380B7E398B0E691"

flags = b''

f = open("./enc", "r")
content = f.read()
f.close()

for encStr in content:
    num = hex(ord(encStr))
    flags += bytes([int(num[2:4], 16), int(num[4:], 16)])

# print(len(content))
print(flags)