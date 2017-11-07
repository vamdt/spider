# -*- coding: UTF-8 -*- 

import re, json, requests, random, base64, os.path, codecs, sys
from bs4 import BeautifulSoup 
from rss import RssBuilder, Channel, ChannelItem
from zaobao_item import ZaoBaoItemParser
import datetime
import time
import email.utils


class Zaobao:

    ZAOBAO_PREFIX = "http://www.zaobao.com"
    list_url = ZAOBAO_PREFIX + "/news/china"

    def __init__(self):
        self.set_encoding()
        self.channel_items = []

    def main(self, page):
        content = self.fetch_list_content(page)
        #file = open('zaobao.html', 'r')
        # content = file.read()
        self.parse_content(content)

    def set_encoding(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')


    def fetch_list_content(self, page):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3213.3 Safari/537.36',
            'Host': 'www.zaobao.com',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Accept-Charset': 'utf-8'
        }
        s = requests.Session()
        s.headers.update(headers)
        url = self.list_url
        if page > 1:
            url = self.list_url + "?page=" + `page`
        print url
        key_r = s.get(url, timeout=5)
        return key_r.content

    def parse_content(self, content):
        html = BeautifulSoup(content, 'html.parser')
        #print html.body.find("div", {"class": "container page-wrapper"})
        post_list = html.body.find_all("div", {"class": "post-detail"})
        print post_list
        for post in post_list:
            title = post.find(class_="post-title").text 
            link = self.ZAOBAO_PREFIX + post.find_parent()["href"] 
            print link
            item = ZaoBaoItemParser().main(link)
            print item["content"][:100]
            channel_item = ChannelItem(title, link, item["content"])
            channel_item.author = item["author"]
            channel_item.pub_date = item["pub_date"]
            self.channel_items.append(channel_item)

    def size(self):
        return len(self.channel_items)

    def contains_item_by_url(self, url):
        for channel_item in self.channel_items:
            if channel_item.link == url:
                return True
        return False

    def first_url(self):
        return self.channel_items[0].link

    def generate(self, file_path):
        channel = Channel()
        channel.title = "联合早报网 - 中国新闻"
        channel.link = "http://www.zaobao.com/news/china"
        channel.description = "联合早报网是海外最重要的权威新闻网站，以第三只眼看大中华，客观新闻和深度评析是众多亚太区读者的最爱。"
        channel.language = "zh-CN"
        now = datetime.datetime.now()
        channel.last_build_date = email.utils.formatdate(time.mktime(now.timetuple()), True)
        channel.image_url = "http://www.zaobao.com/sites/all/themes/zb2016/assets/imgs/zbsg/apple-icon-144x144.png"
        builder = RssBuilder()
        builder.build(channel, self.channel_items)
        builder.write(file_path)
