import math
from gmpy2 import powmod
def getRec(i):
    if i % 2:
        return (2*powmod(3, i, 256)-1) % 256
    else:
        return (2*powmod(3, i, 256)+1) % 256
    # return (int)(2*math.pow(3, i) + pow(-1, i)) % 256
    
flag = ''
keys = [0]*8000

hexString = '7671C5A9E222D8B573F19228B2BF905A7677FCA6B32190DA6FB5CF38'
flags = bytes.fromhex(hexString)

# enc = [0x76, 0x71, 0xC5, 0xA9, 0xE2, 0x22, 0xD8, 0xB5, 0x73, 0xF1, 0x92, 0x28, 0xB2, 0xBF, 0x90, 0x5A, 0x76, 0x77, 0xFC, 0xA6, 0xB3, 0x21, 0x90, 0xDA, 0x6F, 0xB5, 0xCF, 0x38]
for i in range(len(flags)):
    # print(getRec(i*i))
    flag += chr(flags[i] ^ getRec(i*i))

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