import re
import urllib
import json
import os

def main():
    urls = get_urls('http://www.yinwang.org/')
    print urls
    # urls = get_urls('index.tmp')
    # urls_json = json.dumps( urls, sort_keys=True, indent=4, separators=(',', ': ') )
    # file = open('urls.tmp', 'w')
    # file.write( urls_json )
    # file.close()
    dir_str = './download/posts'
    if not os.path.exists(dir_str):
        os.mkdir(dir_str)
    for url in urls:
        file = open(dir_str + '/' + url['name'] +'.html', 'w')
        file.write( get_html(url['url']) )
        file.close

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

if __name__ == '__main__':
    main()