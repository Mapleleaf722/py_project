import requests
from bs4 import BeautifulSoup


class FindBook(object):

    def __init__(self, start_page, end_page):
        # self.base_url = base_url
        self.start = start_page
        self.end = end_page
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/131.0.0.0 Safari/537.36"}

    # 获取单个页面
    def send(self, one_url):
        response = requests.get(one_url, headers=self.headers)
        if response.status_code == 200:
            response.encoding = "gbk"
            return response.text
        else:
            print(f"获取页面失败：{response.status_code}")

    # 数据清洗
    def data_cleansing(self, html):
        soup = BeautifulSoup(html, "html.parser")
        # 查找标题
        title_tag = soup.find('h2', class_='articleH2')
        if title_tag:
            title_all: str = title_tag.get_text(strip=True)
        else:
            title_all = "No Title Found"

        # 查找正文
        text_div = soup.find('div', class_='articleContent')
        if text_div:
            paragraphs = text_div.find_all('p')
            body_text: list = [p.get_text(strip=True) for p in paragraphs]
            body_text: str = '\n\n'.join(body_text)  # 使用双换行符分隔段落
        else:
            body_text: str = "No Body Text Found"
        return "{0}{1}".format(title_all, body_text)

    # 保存单个数据
    def save(self, content, file_name):
        with open(f"{file_name}.txt", "a", encoding="gbk") as f:
            if content:
                f.write(content)

    def run(self):
        for i in range(self.start, self.end - 1, -1):
            # url在这里设置
            self.url = f"https://www.ppzuowen.com/book/maodun/eergunaheyouan/{i}.html"
            self.save(self.data_cleansing(self.send(self.url)), "额尔古纳河右岸（迟子建）")


if __name__ == "__main__":
    start = 547642
    end = 547608
    chizijian = FindBook(start, end)
    chizijian.run()
    input("是否结束程序y/n:")
