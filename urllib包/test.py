import urllib.error
import urllib.request as request

try:
    url = 'http://www.baidu.com/rqerfdfadfad'
    res = request.urlopen(url)
    print(res.read())
except urllib.error.HTTPError as herr:
    print(herr)
except urllib.error.URLError as urlerr:
    print(urlerr)
