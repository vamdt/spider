# encoding=utf-8
import re, urllib, os

site_url='http://songtaste.com/playmusic.php?song_id=2874719,3400819,3236659,3396509,3260763,3401032,3295653,3380110,3362042,3197748,3396442,3051838,2954982,3402048,3340027,3405537,3405559,3028870,3404870,3088088,3402115,310888,3391730,3370179,3396506,3403360,1958838,3405676,2978440,1352773,3399701,3333707,3402918,3340649,3381388,2471940,169832,3320432,3405570,3271120,3405392,255904,1803433,3405510,3287450,3066389,3372969,3039690,3377969,3217564'

def main():
    songs = get_song_infos(site_url)
    download(songs)

def get_song_infos(entry):
    f = urllib.urlopen(entry)
    html = f.read()
    prog = re.compile(r"WrtSongLine\(\"(?P<id>.*)\", \"(?P<name>.*)\", \"(?P<author>.*)\", \".*\", \".*\", \"(?P<url>.*)\", \".*\"\)\;")
    matches = prog.finditer(html)
    infos = []
    for match in matches:
        infos.append({
            'id': match.group('id'),
            'name': match.group('name'),
            'author': match.group('author'),
            'url': match.group('url'),
            })
    return infos

def download(songs):
    for song in songs:
        print song['url']
        name = song['name'] + '-' + song['author'] + '.mp3'
        save(song['url'], name)

def save(obj, name):
    urllib.urlretrieve(obj, name)

if __name__ == '__main__':
    main()