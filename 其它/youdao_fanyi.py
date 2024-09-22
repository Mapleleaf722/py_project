import urllib.parse
import urllib.request

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
data = {
    'from': 'zh',
    'to': 'en',
    'query': '智能学习公司',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '996263.774294',
    'token': '8ec8e38c6e224cea38aba3a6c60bfa0b',
    'domain': 'common',
    'ts': '1695491060644'
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# 对字典数据进行编码
data = bytes(urllib.parse.urlencode(data).encode('utf-8'))
req = urllib.request.Request(url, data=data, headers=header)
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
# 发送请求，得到响应
response = urllib.request.urlopen(url, data=data)
print(response.headers)
# 解码
html = response.read().decode('utf-8')
print(html)
