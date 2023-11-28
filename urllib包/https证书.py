# 1.忽略验证，创建一个不需要验证的证书:ssl._create_unverified_context()
# 2.指明证书(.pem):ssl.create_default_context(cafile='')
import ssl
from urllib import request

url = 'https://www.1234.com'
res = request.urlopen(url, context=ssl.create_default_context(cafile=''))
print(res.read().decode('utf-8'))
