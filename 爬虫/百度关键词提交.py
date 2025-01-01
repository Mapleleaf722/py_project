import requests

url = "https://www.baidu.com/s"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

api_baidu = {'wd': '刘恒'}
r = requests.get(url, params=api_baidu, headers=headers)
print(r.text)
