# 创建蓝图 使用蓝图 注册蓝图
from flask import Blueprint

index_blue = Blueprint('index_blue',__name__)

# 把使用蓝图对象的文件，导入到创建蓝图对象的下面
from . import views