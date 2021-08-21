fib = [1, 1]
for i in range(2, 11):
	fib.append(fib[i - 1] + fib[i - 2])

# print(fib)

def f2c(bits):
    r = 0
    for i in range(11):
        if bits[i] == '1':
            r += fib[10-i]
        else:
            continue
    return chr(r)

f = open("flag.enc", "r")
s = f.read().split()
flag = ""
for item in s:
    flag += f2c(item)
    print(flag)
