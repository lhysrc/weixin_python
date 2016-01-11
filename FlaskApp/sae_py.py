import MySQLdb
import sae
from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
    MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
)

from flask import Flask, g, request
from FlaskApp import  app
#app = Flask(__name__)
#app.debug = True

@app.before_request
def before_request():
    g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
                           MYSQL_DB, port=int(MYSQL_PORT))


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'): g.db.close()

# @app.route('/')
# def hello():
#     return "Hello, I'm LinHy!"

@app.route('/douban', methods=['GET', 'POST'])
def douban():
    return str( dict(request.args))
  



@app.route('/fankui', methods=['GET', 'POST'])
def greeting():
    html = ''

    if request.method == 'POST':
        c = g.db.cursor()
        c.execute("insert into demo(text) values(%s)", (request.form['text']))

    html += """
    <form action="" method="post">
        <div><textarea cols="40" name="text"></textarea></div>
        <div><input type="submit" /></div>
    </form>
    """
    c = g.db.cursor()
    c.execute('select time,content from fankui')
    msgs = list(c.fetchall())
    msgs.reverse()
    for row in msgs:
        #ltime = time.localtime(float(row[0]))
        #dt = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
        #html +=  '<p>' + str(dt) + '<->' + row[-1] + '</p>'
		html +=  '<p>' + row[-1] + '</p>'
    return html