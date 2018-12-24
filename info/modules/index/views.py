from flask import session,render_template,current_app
# 导入蓝图
from . import index_blue


@index_blue.route('/')
def index():
    session['itcast'] = '2018'
    return render_template('news/index.html')


@index_blue.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')