import pandas as pd
import requests
from bs4 import BeautifulSoup


class Douban250(object):

    def __init__(self, url, headers, pages):
        self.kw = None
        self.url = url
        self.headers = headers
        self.pages = pages

    # 获取单个页面
    def send(self):
        response = requests.get(self.url, headers=self.headers, params=self.kw)
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)
    # 数据清洗
    def data_cleansing(self, html):
        soup = BeautifulSoup(html, "html.parser")
        result = soup.find("ol", attrs={"class": 'grid_view'}).find_all("li")
        for i in result:
            title = i.find("span", attrs={"class": 'title'}).text
            other = i.find("span", attrs={"class": 'other'}).text
            rating_num = i.find("span", attrs={"class": 'rating_num'}).text
            intro = i.find("br").find_next_sibling(string=True).strip()
            time = intro.split('/')[0]
            country = intro.split('/')[1]
            tags = intro.split("/")[-1]
            dict1 = dict(title=title, other=other, rating_num=rating_num, time=time, country=country, tags=tags)
            yield dict1

    # 保存单个数据
    def save(self, content: list):
        df = pd.DataFrame(content)
        excel_path = '豆瓣电影 Top 250.xlsx'
        df.to_excel(excel_path, index=False)  # index=False表示不保存行索引

    def run(self):
        d_list = []
        self.kw = {}
        for i in range(self.pages):
            self.kw = {"start": 25 * i}
            for j in self.data_cleansing(self.send()):
                d_list.append(j)
        self.save(d_list)


url = "https://movie.douban.com/top250?"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
douban250 = Douban250(url, headers, 10)

douban250.run()
input("是否结束程序y/n:")
