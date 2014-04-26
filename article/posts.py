import re
import urllib
import json

def main():
    # get_urls('http://www.yinwang.org/')
    urls = get_urls('index.tmp')
    urls_json = json.dumps( urls, sort_keys=True, indent=4, separators=(',', ': ') )
    file = open('urls.tmp', 'w')
    file.write( urls_json )
    file.close()

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