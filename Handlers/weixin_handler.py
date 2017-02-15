#coding:utf-8

from api_handler import *

TOKEN = 'weixin'
def onText(wxmsg):
    '''收到文本
    Content	文本消息内容'''
    inTxt = wxmsg.Content
    #return wxmsg.resp_text(wxmsg['FromUserName'])   
    
    if inTxt.lower().startswith('fy'):    
        return wxmsg.resp_text(youdao(inTxt[2:]))   
    elif inTxt.startswith('?') or inTxt.startswith(u'？'): 
        return wxmsg.resp_text(u'''通过发送以下列字符开头的消息可查询相关信息：
fy  翻译（来自有道）
dy  电影（来自豆瓣）
无前缀默认为查询电影''')
        
    # elif inTxt.startswith('!') or inTxt.startswith(u'！'):
    #     c = g.db.cursor()
    #     c.execute("insert into fankui(userid,time,content) values(%s,%s,%s)", \
    #               (wxmsg['FromUserName'],wxmsg['CreateTime'],inTxt[1:].encode('utf-8')))
    #     return wxmsg.resp_text(u'反馈已记录。')
    
    #c.execute('select content from fankui')
    #msgs = list(c.fetchall())
    #msgs.reverse()
    #res = ''
    #for row in msgs:
    #    res += row[-1] + ','
    #return wxmsg.resp_text(res) 
    
    
     
    else:#
        if inTxt.startswith('dy'):
            inTxt = inTxt[2:]
        newsItems = douban_dianying(inTxt)
        return wxmsg.resp_text(u'找不到') if not newsItems else wxmsg.resp_news(newsItems)
	
    #news1 = NewsItem(wxmsg.Content,youdao(wxmsg.Content),"","")
    #news2 = NewsItem("title2","yyyyyyyyyyy","picurl","url")
    #newsItems = [news1]
    #return wxmsg.resp_news(newsItems)

def onImage(wxmsg):
    '''收到图片
    PicUrl	图片链接
	MediaId	图片消息媒体id，可以调用多媒体文件下载接口拉取数据。'''
    #return wxmsg.resp_music('Sorry','对不起，我还识别不了，来听首歌吧。',r'http://7s1r1i.com1.z0.glb.clouddn.com/小皮%20-%20村庄.mp3','')
    return wxmsg.resp_text(u'对不起，我还识别不了……')

def onVoice(wxmsg): 
    '''收到语音
    MediaId	语音消息媒体id，可以调用多媒体文件下载接口拉取数据。
	Format	语音格式，如amr，speex等
	Recognition为语音识别结果'''
    return wxmsg.resp_text(wxmsg.Recognition if wxmsg.Recognition is not 'None' else u"没听懂……")

def onVideo(wxmsg):
    '''收到视频
    MediaId	视频消息媒体id，可以调用多媒体文件下载接口拉取数据。
	ThumbMediaId	视频消息缩略图的媒体id，可以调用多媒体文件下载接口拉取数据。'''
    return wxmsg.resp_text(u'对不起，我还识别不了……')

def onShortVideo(wxmsg):
    '''收到小视频'''
    return wxmsg.resp_text(u'对不起，我还识别不了……')

def onLocation(wxmsg):
    '''收到位置信息
    Location_X	地理位置维度
	Location_Y	地理位置经度
	Scale	地图缩放大小
	Label	地理位置信息'''
    txt = u"这是您所在位置：\nX:%s\nY:%s" % (wxmsg['Location_X'],wxmsg['Location_Y'])    
    return wxmsg.resp_text(txt)

def onLink(wxmsg):
    '''收到链接
    Title	消息标题
	Description	消息描述
	Url	消息链接'''
    return wxmsg.resp_text('url')
 
def onSubscribe(wxmsg):
    '''关注'''
    return wxmsg.resp_text(u'感谢您的关注。你可以发“?”给我查看帮助。')

def onUnsubscribe(wxmsg):
    '''取消关注'''
    return wxmsg.resp_text(u'oh，漏，你还没说为什么！')

def onScan(wxmsg):
    '''扫描二维码'''
    return wxmsg.resp_text(wxmsg.self.Ticket)

def onClick(wxmsg):
    '''点击菜单拉取消息时 
    EventKey	事件KEY值，与自定义菜单接口中KEY值对应'''
    return wxmsg.resp_text('onClick')

def onEventLocation(wxmsg):
    '''用户同意上报地理位置后，每次进入公众号会话时，都会在进入时上报地理位置
    或在进入会话后每5秒上报一次地理位置，公众号可以在公众平台网站中修改以上设置。
    上报地理位置时，微信会将上报地理位置事件推送到开发者填写的URL
    Latitude	地理位置纬度
	Longitude	地理位置经度
	Precision	地理位置精度'''
    return wxmsg.resp_text('xy')

def onView(wxmsg):
    '''点击菜单跳转链接	
    EventKey	事件KEY值，设置的跳转URL'''
    return wxmsg.resp_text('onView') 
 
 
 
 
