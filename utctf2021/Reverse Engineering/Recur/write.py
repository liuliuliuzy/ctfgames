known = [3, 5]
for i in range(2, 28*28):
    tmp = (2*known[i-1] + 3*known[i-2]) & 0xffffffffffffffff
    known.append(tmp)

before = b'vq\xc5\xa9\xe2"\xd8\xb5s\xf1\x92(\xb2\xbf\x90Zvw\xfc\xa6\xb3!\x90\xdao\xb5\xcf8'
flag = ''
for i in range(28):
    print(known[i*i] % 256)
    flag += chr((before[i] ^ known[i*i]) &0xff)
print(flag)

'''
3
5
163
197
131
69
163
133
3
133
163
69
131
197
163
5
3
5
163
197
131
69
163
133
3
133
163
69
'''