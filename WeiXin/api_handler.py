#coding:utf-8
import urllib2
from urllib import *
import json
import zlib
from WeiXinMsg import *

def getJson(url):
    request = urllib2.Request(url)
    request.add_header('Accept-encoding', 'gzip')
    opener = urllib2.build_opener()
    response = opener.open(request)
    html = response.read()#.decode('gbk').encode('utf-8')
    gzipped = response.headers.get('Content-Encoding')
    if gzipped:
        html = zlib.decompress(html, 16+zlib.MAX_WBITS)    
    return json.loads(html)
    #resp = urllib2.urlopen(url)
    #return json.loads(resp.read())


def douban_dianying(text):
    url = 'http://api.douban.com/v2/movie/search?q=%s' % quote_plus(text.encode('utf-8'))
    description = getJson(url)
    
    if description['total'] is 0:
        return ''
    res = description['subjects']
    items = []
    for i in res:
        title = i['title']
        rating = i['rating']['average']
        picurl = i['images']['medium']
        url = i['alt']
        genres = '|'.join(i['genres'])
        items.append(NewsItem("%s (%s)" % (title,rating),'',picurl,url))
    return items[:5]
    