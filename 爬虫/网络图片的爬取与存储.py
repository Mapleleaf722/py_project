import os

import requests

url = 'http://img0.dili360.com/ga/M02/33/7C/wKgBzFSbqQyAJVAuAARB8cSWH_w695.tub.jpg@!rw14'
root = 'images/'
path = root + url.split('/')[-1][:-6]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    elif not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print("爬取失败")
