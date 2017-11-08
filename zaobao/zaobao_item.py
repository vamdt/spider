# -*- coding: UTF-8 -*- 

import re, json, requests, random, base64, os.path, codecs, sys
import datetime
from bs4 import BeautifulSoup 
import string
import email.utils

class ZaoBaoItemParser:
    def main(self, url):
        self.set_encoding()
        content = self.fetch_item_content(url)
        # file = open('zaobao_item.html', 'r')
        # content = file.read()
        self.item = {}
        self.parse_content(content)
        return self.item

    def set_encoding(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')


    def fetch_item_content(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3213.3 Safari/537.36',
            'Host': 'www.zaobao.com',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Accept-Charset': 'utf-8'
            }
        s = requests.Session()
        s.headers.update(headers)
        key_r = s.get(url, timeout=10)
        return key_r.content

    def parse_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        soup.find(id="imu").extract()
        content = soup.find(class_="article-content-container")
        author = ""
        author_el = soup.find(class_="contributor")
        if author_el is not None:
            author = author_el.text
        pub_date = soup.find(class_="datestamp").text
        self.item["content"] = str(content)
        self.item["author"] = author.replace("文/", "")
        self.item["pub_date"] =self.parse_date(pub_date)

    def parse_date(self, date_str):
        import re, time
        date_str_without_week = re.sub(ur"\s+星期(?u)\w", "", date_str)
        dt = datetime.datetime.strptime(date_str_without_week, u"%Y年%m月%d日 %I:%M %p")
        return email.utils.formatdate(time.mktime(dt.timetuple()), True)

    html_escape_table = {
            "&": "&amp;",
            '"': "&quot;",
            "'": "&apos;",
            ">": "&gt;",
            "<": "&lt;",
            }

    def html_escape(self, raw):
        return "".join(self.html_escape_table.get(c, c) for c in raw)
