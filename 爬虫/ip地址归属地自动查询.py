import requests

try:
    url = "https://www.ipshudi.com/"
    ip_address = "202.204.80.112"
    r = requests.get(url + ip_address + '.htm', headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"},
                     timeout=5)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except TimeoutError:
    print('连接超时')
except:
    print('爬取失败')
