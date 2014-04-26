import re
import urllib
import json
import os

BASE_DOWN_DIR = './download'
BASE_DOWN_POSTS_DIR = BASE_DOWN_DIR + '/posts'
def main():
    urls = get_urls('http://www.yinwang.org/')

    if not os.path.exists(BASE_DOWN_POSTS_DIR):
        os.makedirs(BASE_DOWN_POSTS_DIR)

    save_as_json(urls, BASE_DOWN_POSTS_DIR + '/urls.json')
    urls = urls[0:1]
    save_posts(urls)
    

def get_urls(entry):
    urls = []
    f = urllib.urlopen(entry)
    html = f.read()
    pattern = re.compile(u'<a href="(http://yinwang.org/blog-cn/.*?)">(.*?)</a>', re.DOTALL)
    url_wrappers = pattern.findall( html )
    for url_wrapper in url_wrappers:
        urls.append( {'name': url_wrapper[1], 'url': url_wrapper[0]} )
    return urls

def get_html(url):
    return urllib.urlopen(url).read()

def save_posts(urls):
    for url in urls:
        html = get_html(url['url'])
        file_name = BASE_DOWN_POSTS_DIR + '/' + url['name'] +'.html'
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