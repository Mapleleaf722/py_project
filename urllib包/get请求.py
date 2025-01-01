from urllib import request

# url_img = 'http://v6.huanqiucdn.cn/4394989evodtranscq1500012236/d97faeb05576678021659148128/v.f100830.mp4'
#
#
# res = request.urlopen(url_img)
# with open('网络请求/123.mp4', 'wb') as f:
#     f.write(res.read())


url = 'http://www.wakey.com.cn/'
res = request.urlopen(url)
# 文件编码和请求结果的解码需要保持一致
with open('网络请求/index.html', 'w', encoding='utf-8') as f:
    f.write(res.read().decode('utf-8'))
