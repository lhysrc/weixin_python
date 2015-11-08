#coding:utf-8

import xml.etree.ElementTree as ET
import time


class NewsItem(object):
    def __init__(self, title,desc,pic_url,url):
        self.title = title
        self.desc = desc
        self.pic_url = pic_url
        self.url = url
    def __str__(self):
        template = '''<item>
<Title><![CDATA[%s]]></Title>
<Description><![CDATA[%s]]></Description>
<PicUrl><![CDATA[%s]]></PicUrl>
<Url><![CDATA[%s]]></Url>
</item>'''
        return template % (self.title,self.desc,self.pic_url,self.url)



class WeiXinMsg(object):
    def __init__(self, xml_body=None):
        self.xml_body = unicode(xml_body).encode("utf-8")
        root = ET.fromstring(self.xml_body)

        self.j={}
        for child in root:
            if child.tag == 'CreateTime':
                value = long(child.text)
            else:
                value = child.text
            self.j[child.tag] = value
        self.ToUserName = self.j['FromUserName']
        self.FromUserName = self.j['ToUserName']
        self.MsgType = self.j['MsgType']
        
        self.MsgId = self.j['MsgId'] if self.j.has_key('MsgId') else ''        
        self.Content = self.j['Content'] if self.j.has_key('Content') else ''
        self.PicUrl = self.j['PicUrl'] if self.j.has_key('PicUrl') else ''
        self.MediaId = self.j['MediaId'] if self.j.has_key('MediaId') else ''
        self.Recognition = self.j['Recognition'] if self.j.has_key('Recognition') else ''
        self.Format = self.j['Format'] if self.j.has_key('Format') else ''
        self.ThumbMediaId = self.j['ThumbMediaId'] if self.j.has_key('ThumbMediaId') else ''
        self.Location_X = self.j['Location_X'] if self.j.has_key('Location_X') else ''
        self.Location_Y = self.j['Location_Y'] if self.j.has_key('Location_Y') else ''
        self.Scale = self.j['Scale'] if self.j.has_key('Scale') else ''
        self.Label = self.j['Label'] if self.j.has_key('Label') else ''
        self.Title = self.j['Title'] if self.j.has_key('Title') else ''
        self.Description = self.j['Description'] if self.j.has_key('Description') else ''
        self.Url = self.j['Url'] if self.j.has_key('Url') else ''       
        self.EventKey = self.j['EventKey'] if self.j.has_key('EventKey') else ''
        self.Event = self.j['Event'].lower() if self.j.has_key('Event') else ''
        self.Ticket = self.j['Ticket'].lower() if self.j.has_key('Ticket') else ''

# # ToUserName  开发者微信号
# # FromUserName    发送方帐号（一个OpenID）
# # CreateTime  消息创建时间 （整型）
# # MsgType 消息类型
# # Content 文本消息内容
# # MsgId   消息id，64位整型      

# # PicUrl  图片链接
# # MediaId 图片消息媒体id，可以调用多媒体文件下载接口拉取数据。
# # MediaId 语音消息媒体id，可以调用多媒体文件下载接口拉取数据。
# # Format  语音格式，如amr，speex等
# # MediaId 视频消息媒体id，可以调用多媒体文件下载接口拉取数据。
# # ThumbMediaId    视频消息缩略图的媒体id，可以调用多媒体文件下载接口拉取数据。
# # MediaId 视频消息媒体id，可以调用多媒体文件下载接口拉取数据。
# # ThumbMediaId    视频消息缩略图的媒体id，可以调用多媒体文件下载接口拉取数据。
# # Location_X  地理位置维度
# # Location_Y  地理位置经度
# # Scale   地图缩放大小
# # Label   地理位置信息
# # Title   消息标题
# # Description 消息描述
# # Url 消息链接


    def __getitem__(self,name):
        return self.j[name] if self.j.has_key(name) else ''

            
    def resp_text(self,text,funcFlag=0):
        template = '''<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
<FuncFlag>%s</FuncFlag>
</xml>'''
        return template % (self.ToUserName,self.FromUserName,int(time.time()),text,funcFlag)

        
    def resp_news(self,news_items,funcFlag=0):
        template='''<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>%s</ArticleCount>
<Articles>
  %s
</Articles>
<FuncFlag>%s</FuncFlag>
</xml>'''
        return template % (self.ToUserName,self.FromUserName,int(time.time()),len(news_items),\
        (''.join([str(i) for i in news_items])),funcFlag)


        
    def resp_music(self,title,desc,music_url,hqmusic_url,funcFlag=0):
        '''回复音乐'''
        template='''<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[music]]></MsgType>
<Music>
  <Title><![CDATA[%s]]></Title>
  <Description><![CDATA[%s]]></Description>
  <MusicUrl><![CDATA[%s]]></MusicUrl>
  <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
</Music>
<FuncFlag>%s</FuncFlag>
</xml>'''
        return template % (self.ToUserName,self.FromUserName,int(time.time()),\
        title,desc,music_url,hqmusic_url,funcFlag)
            
        
        
