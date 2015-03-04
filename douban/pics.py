# coding=utf-8

import re
import urllib
import json
import os, random

BASE_DOWN_DIR = './download'
BASE_DOWN_POSTS_DIR = BASE_DOWN_DIR + '/posts'
BASE_URL = 'http://www.douban.com/photos/photo/2230938262/'

class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.4 Safari/537.36"

urllib._urlopener = AppURLopener()


def main():
    i = 0;
    url = BASE_URL;
    while(i<3):
        i = i+1;
        url = play(url, i);

def play(url, index):
    f = urllib.urlopen(url)
    html = f.read()
    print html
    pattern = re.compile(u'<a href="(http://www.douban.com/photos/photo/\d+/#image)" title=".+" id="next_photo">.+</a>',re.DOTALL)
    url = pattern.findall(html)[0]
    p2 = re.compile(u'<a class="mainphoto" href="\S+" title="\S+">\s+<img src="(http://img.+\.douban\.com/view/photo/photo/public/.+\.jpg)" />\s+</a>', re.DOTALL)
    img_url = p2.findall(html)[0]
    print img_url
    create_dirs(BASE_DOWN_POSTS_DIR)
    save_posts(img_url, index)
    return url


def get_html(url):
    return urllib.urlopen(url).read()

def create_dirs(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def save_posts(url, index):
    html = get_html(url)
    file_name = BASE_DOWN_POSTS_DIR + '/' + str(index) + '.jpg'
    save( html, file_name)

def save(obj, name):
    file = open(name, 'w')
    file.write(str(obj))
    file.close


def save_as_json(obj, name):
    json_data = json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    save(json_data, name)

if __name__ == '__main__':
    main()