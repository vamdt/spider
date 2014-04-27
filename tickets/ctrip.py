# -*- coding: UTF-8 -*- 

import re, urllib, urllib2, cookielib,json

# site_url = 'http://flights.ctrip.com/international/beijing-taipei-bjs-tpe'
site_url = 'http://flights.ctrip.com/international/beijing-kualalumpur-bjs-kul'

search_url = 'http://flights.ctrip.com/international/GetSubstepSearchResults.aspx?IsJSON=T&queryLogTransNo=3914042718000006946&QueryType=1&cityPairAirline=first&withDirectAirline=T&RdNo=2103213618&sPassType=NOR&ind=742,752,774,754'

# Set-Cookie:ASP.NET_SessionId=i0szmvqc0usatrlaffjsfvim; path=/; HttpOnly
# Set-Cookie:AX-20480-flights_international=FAACAIAKFAAA; Path=/

def main():
    cookies = cookielib.LWPCookieJar()
    opener = urllib2.build_opener( urllib2.HTTPCookieProcessor(cookies) )
    urllib2.install_opener(opener)
    req = urllib2.Request(site_url)
    param = urllib.urlencode({'DDatePeriod1': '2014-05-12'})
    html = urllib2.urlopen(req, param)
    # print html.info()
    for cookie in cookies:
        print cookie.name, cookie.value

    search_req = urllib2.Request(search_url)
    search_html = urllib2.urlopen(search_req)
    raw_str = search_html.read()
    save(raw_str, 'raw_ctrip.txt')

    data = json.loads(raw_str.decode('latin1'))
    save_as_json(data, 'ctrip.txt')

    cookies.save('ctrip_cookie.txt')

def save(obj, name):
    file = open(name, 'w')
    file.write(str(obj))
    file.close

def save_as_json(obj, name):
    json_data = json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    save(json_data, name)

if __name__ == '__main__':
    main()