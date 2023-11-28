import urllib.request

url = 'http://placekitten.com/g/500/500'
# 得到网页（二进制形式）
response = urllib.request.urlopen(url)
cat_jpg = response.read()
# 格式化文件名
filename = f'{url[-7:-4]}_{url[-3:]}'
with open(f'cat_{filename}.jpg', 'wb') as f:
    f.write(cat_jpg)
