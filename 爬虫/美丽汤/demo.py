import bs4
import requests
from bs4 import BeautifulSoup

try:
    url = 'http://python123.io/ws/demo.html'
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    # print(soup.prettify())
    for i in soup.find_all('p', attrs={"class": 'course'})[0]:
        if isinstance(i, bs4.element.NavigableString):
            print(i, type(i))
            with open('天之下.txt', 'a', encoding='utf-8') as f:
                f.write(i)
except:
    print('爬取失败')
