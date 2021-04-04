# f = open('./secret.txt')
# x = ''
# while True:
#     s = f.read(8)
#     if not s:
#         break
#     x += chr(int(s, 2))
#     s = f.read(1)
#     if not s:
#         break
# print(x)

# f.close()
# =============================Cipher Cauntlet================================
# import base64
# c = b'TmV3IGNoYWxsZW5nZSEgQ2FuIHlvdSBmaWd1cmUgb3V0IHdoYXQncyBnb2luZyBvbiBoZXJlPyBJdCBsb29rcyBsaWtlIHRoZSBsZXR0ZXJzIGFyZSBzaGlmdGVkIGJ5IHNvbWUgY29uc3RhbnQuIChoaW50OiB5b3UgbWlnaHQgd2FudCB0byBzdGFydCBsb29raW5nIHVwIFJvbWFuIHBlb3BsZSkuCm15eHFia2Rldmtkc3l4YyEgaXllIHJrZm8gcHN4c2Nyb24gZHJvIGxvcXN4eG9iIG1iaXpkeXFia3pyaSBtcmt2dm94cW8uIHJvYm8gc2MgayBwdmtxIHB5YiBrdnYgaXllYiBya2JuIG9wcHliZGM6IGVkcHZrcXt4eWdfaXllYm9fenZraXN4cV9nc2RyX21iaXpkeX0uIGl5ZSBnc3Z2IHBzeG4gZHJrZCBrIHZ5ZCB5cCBtYml6ZHlxYmt6cmkgc2MgbGVzdm5zeHEgeXBwIGRyc2MgY3liZCB5cCBsa2NzbSB1eHlndm9ucW8sIGt4biBzZCBib2t2dmkgc2MgeHlkIGN5IGxrbiBrcGRvYiBrdnYuIHJ5em8gaXllIG94dHlpb24gZHJvIG1ya3Z2b3hxbyE='
# print(base64.b64decode(c))

# flag = ''
# cf = 'edpvkq{xyg_iyebo_zvkisxq_gsdr_mbizdy}'
# for i in cf:
#     if i == '_' or i == '{' or i == '}':
#         flag += i
#         continue
#     tmp = ord(i) + ord('u') - ord('e')
#     if tmp > ord('z'):
#         tmp -= 26
#     flag += chr(tmp)

# print(flag)

# =============================Sizzling Bacon================================

s = 'sSsSSsSSssSSsSsSsSssSSSSSSSssS{SSSsSsSSSsSsSSSsSSsSSssssssSSSSSSSsSSSSSSSSsSSsssSSssSsSSSsSSsSSSSssssSSsssSSsSSsSSSs}'
def generate_dict():

    """
    Create Bacon dictionary.
    a   AAAAA   g     AABBA   n    ABBAA   t     BAABA
    b   AAAAB   h     AABBB   o    ABBAB   u-v   BAABB
    c   AAABA   i-j   ABAAA   p    ABBBA   w     BABAA
    d   AAABB   k     ABAAB   q    ABBBB   x     BABAB
    e   AABAA   l     ABABA   r    BAAAA   y     BABBA
    f   AABAB   m     ABABB   s    BAAAB   z     BABBB
    :return: Bacon dict
    """

    bacon_dict = {}

    for i in range(0, 26):
        tmp = bin(i)[2:].zfill(5)
        tmp = tmp.replace('0', 'S')
        tmp = tmp.replace('1', 's')
        bacon_dict[tmp] = chr(97 + i)

    return bacon_dict

dic = generate_dict()
# anodict = {'s': 'b', 'S': 'a'}
# print(dic)

i = 0
flag = ''
while i < len(s):
    if s[i] in ['{', '}']:
        flag += s[i]
        i += 1
        continue
    flag += dic[s[i:i+5]]
    i += 5
print(flag)
    
