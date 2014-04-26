import re
import urllib

def main():
    # get_urls('http://www.yinwang.org/')
    urls = get_urls('index.tmp')
    
def get_urls(entry):
    urls = []
    f = urllib.urlopen(entry)
    html = f.read()
    pattern = re.compile(u'<a href="(http://yinwang.org/blog-cn/.*?)>(.*?)</a>', re.DOTALL)
    url_wrappers = pattern.findall( html )
    for url_wrapper in url_wrappers:
        urls.append( {'name': url_wrapper[1], 'url': url_wrapper[0]} )
    return urls

if __name__ == '__main__':
    main()