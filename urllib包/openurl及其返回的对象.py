import urllib.request

url = 'http://www.wakey.com.cn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(url_img)
response = urllib.request.urlopen(req)
print(response)

# print(response.read().decode('utf-8'))
print(f'response.status: {response.status}')
print(f'response.reason: {response.reason}')
print(f'response.msg: {response.msg}')
print(f'response.version: {response.version}')
print(f'response.debuglevel: {response.debuglevel}')
print(f'response.getheaders(): {response.getheaders()}')
print(f'response.getheader("Date"): {response.getheader("Date")}')
print(f'response.geturl(): {response.geturl()}')

urllib.request.urlretrieve()

