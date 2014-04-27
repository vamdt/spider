# encoding=utf-8

import re, urllib, urllib2, cookielib

site_url = 'http://flights.ctrip.com/international/beijing-taipei-bjs-tpe'

# Set-Cookie:ASP.NET_SessionId=i0szmvqc0usatrlaffjsfvim; path=/; HttpOnly
# Set-Cookie:AX-20480-flights_international=FAACAIAKFAAA; Path=/

def main():
    cookies = cookielib.LWPCookieJar()
    opener = urllib2.build_opener( urllib2.HTTPCookieProcessor(cookies) )
    urllib2.install_opener(opener)
    req = urllib2.Request(site_url)
    html = urllib2.urlopen(req)
    print html.info()
    for cookie in cookies:
        print cookie.name, cookie.value


if __name__ == '__main__':
    main()