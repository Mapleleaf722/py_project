import requests

url = ("https://cn-tj-cu-01-17.bilivideo.com/upgcxcode/59/38/1564233859/1564233859-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1717078460&gen=playurlv2&os=bcache&oi=1873267188&trid=0000300d37b38ce34f7a89ccb381da11a4c7u&mid=43704301&platform=pc&og=hw&upsig=7a619456ffcbaabc030b878b3cc5aab7&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=87217&bvc=vod&nettype=0&orderid=0,3&buvid=632EB577-42DF-FAE9-36A7-48372CA74DA708469infoc&build=0&f=u_0_0&agrr=0&bw=74678&logo=80000000")
res = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
print(res.status_code)
open('xxx.mp4', 'wb').write(res.content)
