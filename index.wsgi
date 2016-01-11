#coding:utf-8
#def application(environ, start_response):
#    start_response('200 ok', [('content-type', 'text/plain')])
#    return ['Hello, SAE!']

from FlaskApp import app,sae_py

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



import threading

application = sae_py.sae.create_wsgi_app(app)
#app.run()
