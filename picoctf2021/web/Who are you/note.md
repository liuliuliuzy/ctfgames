一步步修改header

- `User-Agent`：
- `referer`：
- `date`：
- `dnt`：
- `x-forwarded-for`： `94.234.42.81`是一个瑞典的ip地址
- `Accept-Language`：


burp repeater 里的配置：
```
GET / HTTP/1.1
Host: mercury.picoctf.net:1270
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: PicoBrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: sv-SE
referer: http://mercury.picoctf.net:1270/
date: Tue, 15 Nov 2018 08:12:31 GMT
dnt: 1
x-forwarded-for: 94.234.42.81
Connection: close
```