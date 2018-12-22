from flask import session
from . import index_blue

@index_blue.route('/')
def index():
    session['itcast'] = 2018
    return 'hello world'