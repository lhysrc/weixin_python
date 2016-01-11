#coding:utf-8


from WeiXinCore.WeiXinMsg import *


weixin = WeiXinMsg(u'''
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1357290913</CreateTime>
<MsgType><![CDATA[voice]]></MsgType>
<MediaId><![CDATA[media_id]]></MediaId>
<Format><![CDATA[Format]]></Format>
<Recognition><![CDATA[腾讯微信团队]]></Recognition>
<MsgId>1234567890123456</MsgId>
</xml>
''')

def onEvent(wxmsg):
    print 'event'

def onText(wxmsg):
    print 'text'

def onImage(wxmsg):
    pass
def onVoice(wxmsg):
    print 'voice'
def onLocation(wxmsg):
    pass

def onLink(wxmsg):
    pass
Response = {
    "event":onEvent,
    "text":onText,
    "voice":onVoice,

    }

print '\n'.join([k+':'+str(v) for k,v in weixin.j.items()])

print weixin['MsgType']


print weixin.j['MsgType']


Response[weixin.MsgType]()









# news1 = NewsItem("title1","wwwwwwwwwwwwwww","picurl1","url")
# news2 = NewsItem("title2","wwwwwwwwwwwwwww","picurl2","url")
# news3 = NewsItem("title3","wwwwwwwwwwwwwww","picurl3","url")

# news_items = [news1,news2,news3]

# print ''.join([str(i) for i in news_items])

