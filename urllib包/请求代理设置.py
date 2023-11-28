# 同一个IP在高频率请求同一个网站的时侯可能会被网站反爬虫机制屏蔽，这时侯需要大量代理IP参与
# 在高频率请求时不断的更换IP即可
# IP代理设置分为:公开代理和私密代理
# 首先创建一个Handler处理器，然后编译成opener对象，最后使用opener对象直接发送网络请求
import random
from urllib import request

url = 'http://www.whatismyip.com.tw/'
iplist = ['121.8.215.106:9797', '221.226.75.86:55443','183.247.152.98:53281']
# 参数是一个字典
handler = request.ProxyHandler({'http': random.choice(iplist)})
# 定制、创建一个opener
opener = request.build_opener(handler)

opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')]
# 安装opener
request.install_opener(opener)
res = request.urlopen(url)
print(res.read().decode('utf-8'))
