from flask import Flask
app = Flask(__name__)

import FlaskApp.views
from WeiXinCore.WeiXin import echo
try:
    import sae
    import FlaskApp.sae_py
except:
    print("no in sae.")