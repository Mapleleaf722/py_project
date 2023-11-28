from urllib import request

url = 'https://www.baidu.com'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
req = request.Request(url,headers=header)
res = request.urlopen(req)
print(res.read().decode('utf-8'))
