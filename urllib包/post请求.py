import json
from urllib import request, parse

# url_img = 'https://study.163com/mob/seanch/independent/v2'
# dict1 = {}
# data = parse.urlencode(dict1)
# req = request.Request(url_img)


# url_img = 'https://v0.yiketianqi.com/api?unescape=1&version=v61&appid=78811367&appsecret=3V9v2t7w'
# res = request.urlopen(url_img)
# f = res.read().decode('utf-8')
# print(json.loads(f))
# print(json.loads(f)['city'])


url = "https://v0.yiketianqi.com/api"
data = {"unescape": "1", "version": "v61", "appid": "78811367", "appsecret": "3V9v2t7w"}
data = parse.urlencode(data, encoding='utf-8')
print(data)
res = request.urlopen(url, data=bytes(data, encoding='utf-8'))
f = res.read().decode('utf-8')
print(json.loads(f))

