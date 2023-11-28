import urllib.error
from urllib import request

# req = request.Request('http://www.ooxxfishc.com')
# try:
#     request.urlopen(req)
# except urllib.error.URLError as e:
#     print(e.reason)
#     print(e)
#     print(type(e))
req = request.Request('http://www.fishc.com/ooxx.html')
try:
    request.urlopen(req)
except urllib.error.HTTPError as e:
    print(f"返回结果：{e}", f"结果的类型:{type(e)}", sep='\n')
    print(e.code)
    # 打印错误页面（html)
    print(e.read())
except urllib.error.URLError as f:
    print(f.reason)
    print(f"返回结果：{f}", f"结果的类型:{type(f)}", sep='\n')
