import requests
from bs4 import BeautifulSoup

url = "https://imgsmall.idmzj.com/y/20926/41917/2.jpg"
params = "41917.html"


class YaoShenJi(object):
    def __init__(self, url, params):
        self.url = url
        self.params = params

    # 获取页面
    def get_one_html(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/131.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers, params=self.params)
        return response.text

    # 解析内容，并返回图片
    def get_img(self, html):
        soup = BeautifulSoup(html, "html.parser")

        return img

    # 保存图片至文件夹
    def save_img(self, img):
        pass
