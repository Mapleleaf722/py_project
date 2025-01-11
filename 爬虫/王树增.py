import requests
from bs4 import BeautifulSoup


class Find_book(object):

    def __init__(self, base_url, headers, params):
        self.base_url = base_url
        self.headers = headers
        self.params = params

    # 获取单个页面
    def send(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:

            return response.text
        else:
            print(f"获取页面是失败：{response.status_code}")

    # 数据清洗
    def data_cleansing(self, html):
        soup = BeautifulSoup(html, "html.parser")
        # 查找标题
        title_tag = soup.find('h1', class_='news_title')
        if title_tag:
            title_all: str = title_tag.get_text(strip=True)
        else:
            title_all = "No Title Found"

        # 查找正文
        text_div = soup.find('div', id='TextContent')
        if text_div:
            paragraphs = text_div.find_all('p')
            body_text: list = [p.get_text(strip=True) for p in paragraphs]
            body_text: str = '\n\n'.join(body_text)  # 使用双换行符分隔段落
        else:
            body_text: str = "No Body Text Found"
        return "{0}{1}".format(title_all, body_text)

    # 保存单个数据
    def save(self, content):
        with open("额尔古纳河右岸（迟子建）.txt", "a",encoding="utf-8") as f:
            if content:
                f.write(content)

    def run(self):
        for i in range(self.params, 171735):
            self.url = f"https://eergunaheyouan.chibaba.cn/{i}.html"
            self.save(self.data_cleansing(self.send()))


if __name__ == "__main__":
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    params = 171707
    url = f"http://www.ailcai.com/zhanzhengjunshi/4280/{params}.html"
    wangshuzeng = Find_book(url, headers, params)
    wangshuzeng.run()
    input("是否结束程序y/n:")
