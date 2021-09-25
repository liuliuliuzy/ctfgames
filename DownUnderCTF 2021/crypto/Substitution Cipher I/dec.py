import string
def sub(x):
    return 13*x*x + 3*x + 7
dic = {}
for c in string.printable:
    # print(c, ord(c), hex(sub(ord(c))))
    dic[sub(ord(c))] = c

f = open('./output.txt', 'r')
flag = ''
while True:
    c = f.read(1)
    if not c or ord(c)==10:
        break
    # print(ord(c))
    flag += dic[ord(c)]
f.close()
print(flag)