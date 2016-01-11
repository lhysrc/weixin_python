#import WeiXinCore.WeiXin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from FlaskApp import app


app.run(debug=True,port=5000)




