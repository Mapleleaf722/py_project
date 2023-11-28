# 目标：获取淘宝搜索页面的信息，提取其中的商品名称和价格。
# 理解：1.要获得淘宝的搜索接口；2.翻页的处理
# 技术路线：requests-re
# 程序的结构设计
# 步骤1: 提交商品搜索请求，循环获取页面
# 步骤2: 对于每个页面，提取商品名称和价格信息。
# 步骤3: 将信息输出到屏幕上。
import requests


# 获取单个页面
def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                      "Safari/537.36"}
    try:
        respose = requests.get(url, headers=headers, timeout=30)
        respose.raise_for_status()
        respose.encoding = respose.apparent_encoding
        return respose.text
    except:
        print("爬取失败")


# 解析页面，得到商品名称和价格
def parse_page(html, goods_list):
    pass


def print_goods_list():
    pass


def main():
    goods = '书包'
    depth = 2
    url_root = 'https://s.taobao.com/search'
    info_list = []
    for i in range(depth):
        try:
            url = url_root + 'q=书包' + str(44 * i)
            html = get_html(url)
            parse_page(info_list, html)
        except:
            continue
    print_goods_list(info_list)

# main()
