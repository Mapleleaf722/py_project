import re
from urllib import request


def open_url(url):
    req = request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    return html


def get_ip(html_str):
    re_rule = re.compile(
        r'((?:(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5]))[^0-9]')
    iplist = re_rule.findall(html_str)
    for each in iplist:
        print(each)


url = 'https://www.89ip.cn/'
html = open_url(url)
get_ip(html)
