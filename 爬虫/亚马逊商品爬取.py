import requests

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.headers)
    # print(r.text)
except:
    print("爬取失败")
