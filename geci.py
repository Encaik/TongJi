import requests
from bs4 import BeautifulSoup
import json
import re


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/51.0.2704.103 Safari/537.36',
        'Referer': 'http://music.163.com',
        'Host': 'music.163.com'
    }
    try:
        response = requests.get(url, headers = headers)
        html = response.text
        return html
    except:
        print('request error')
        pass


def getSingerInfo(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('ul', class_='f-hide').find_all('a')
    song_Ids = []
    song_Names = []
    for link in links:
        song_Id = link.get('href').split('=')[-1]
        song_Name = link.get_text()
        song_Ids.append(song_Id)
        song_Names.append(song_Name)
    return zip(song_Names, song_Ids)


def getLyric(song_Id):
    url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_Id) + '&lv=1&kv=1&tv=-1'
    try:
        html = getHtml(url)
        json_obj = json.loads(html)
        try:
            initial_lyric = json_obj['lrc']['lyric']
            regex = re.compile(r'\[.*\]')
            final_lyric = re.sub(regex, '', initial_lyric).strip()
            return final_lyric
        except:
            return ""
    except:
        pass


def writeText(song_Name, lyric):
    print(song_Name)
    try:
        if(lyric == ''):
            pass
        else:
            with open("{}.txt".format(song_Name), 'a', encoding='utf-8', errors='ignore') as fp:
                fp.write(lyric)
    except:
        pass


if __name__ == '__main__':
    singer_id = input('请输入歌手ID：')
    start_url = 'http://music.163.com/artist?id={}'.format(singer_id)
    html = getHtml(start_url)
    singer_infos = getSingerInfo(html)
    for singer_info in singer_infos:
        lyric = getLyric(singer_info[1])
        writeText(singer_info[0], lyric)
