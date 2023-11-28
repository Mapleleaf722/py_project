import urllib.request

url = 'https://static.wikia.nocookie.net/oxygennotincluded/images/4/43/%E6%9C%BA%E6%A2%B0%E6%B0%94%E9%97%B8.png/revision/latest?cb=20210531073457&path-prefix=zh'

# # 方法一
# res = urllib.request.urlopen(url)
# with open('网络请求/机械气闸1.jpg', 'wb') as f:
#     f.write(res.read())

# 方法二
urllib.request.urlretrieve(url, '网络请求/机械气闸2.jpg')
