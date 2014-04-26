import re
import urllib
import json
import os

def main():
    urls = get_urls('http://www.yinwang.org/')
    dir_str = './downloads/posts'

    if not os.path.exists(dir_str):
        os.makedirs(dir_str)

    save_as_json(urls, dir_str + '/urls.json')
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
    dir_str = './downloads/posts'
    for url in urls:
        html = get_html(url['url'])
        file_name = dir_str + '/' + url['name'] +'.html'
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