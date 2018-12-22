from flask import session
# 导入蓝图
from . import index_blue

@index_blue.route('/')
def index():
    session['itcast'] = '2018'
    return 'hello world'