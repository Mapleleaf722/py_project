import re
from urllib import request


def get_html(url_):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    req = request.Request(url_, headers=header)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    return html


# print(get_html(url))
def data_clean(html):
    p = re.compile(r'<img class="BDE_Image" src="([^"]+\.jpg[^"]+)"')
    urls = p.findall(html_tieba)
    return urls


url = 'https://tieba.baidu.com/p/6719881386'
html_tieba = get_html(url)
jpg_urls = data_clean(html_tieba)

a = 1
for i in jpg_urls:
    filename = f'{a}.jpg'
    a += 1
    response = request.urlopen(i)
    with open(f'和谐过的皮肤/{filename}', 'wb') as f:
        f.write(response.read())

for i in range(2, 11):
    url_pages = f'{url}?pn={i}'
    html_tieba = get_html(url_pages)
    jpg_urls = data_clean(html_tieba)
    for j in jpg_urls:
        filename = f'{a}.jpg'
        a += 1
        response = request.urlopen(j)
        with open(f'和谐过的皮肤/{filename}', 'wb') as f:
            f.write(response.read())
