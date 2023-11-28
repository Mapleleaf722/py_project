import bs4
import requests
from bs4 import BeautifulSoup


# 获取页面
def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.status_code)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取网页失败！"


# 解析页面并返回字符串
def one_chapter(html):
    line_list = []
    soup = BeautifulSoup(html, 'html.parser')
    lines = soup.find_all('p')
    for line in lines[0].children:
        if isinstance(line, bs4.element.NavigableString):
            line_list.append(line)
    return line_list


# 写入txt文件
def write_in_txt(line_list: 'list'):
    with open('全频段阻塞干扰.txt', 'a', encoding='utf-8') as f:
        for i in line_list:
            f.write(i)


url_root = 'https://www.xyyuedu.com/writer/liucixin/quanpinduanzusaiganrao/'
for i in range(269442, 269452):
    url = url_root + str(i) + '.html'
    html = get_html(url)
    result = one_chapter(html)
    write_in_txt(result)
