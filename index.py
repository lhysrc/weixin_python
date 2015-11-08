#def application(environ, start_response):
#    start_response('200 ok', [('content-type', 'text/plain')])
#    return ['Hello, SAE!']
#import sae
from myapp import app

import WeiXin.WeiXin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#application = sae.create_wsgi_app(app)
app.run()