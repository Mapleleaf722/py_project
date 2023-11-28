import bs4
import requests
from bs4 import BeautifulSoup


# 输人:大学排名URL链接
# 输出: 大学排名信息的屏幕输出( 排名，大学名称总分 )
# 从网络上获取大学排名网页内容
def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


# 提取网页内容中信息到合适的数据结构
def fill_univ_list(ulist: "list", html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        # 检测tr的类型，确定其为标签类型再继续执行
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string.strip(), tds[1]('a')[0].string.strip(), tds[4].string.strip()])


# 利用数据结构展示并输出结果
def print_univ_list(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format('排名', '学校', '总分', chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2023'
    html = get_html_text(url)
    fill_univ_list(uinfo, html)
    print_univ_list(uinfo, 20)


main()
