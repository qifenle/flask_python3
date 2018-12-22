# 创建蓝图对象 使用蓝图对象 注册蓝图对象
from  flask import Blueprint

index_blue = Blueprint('index_blue',__name__)


# 把使用蓝图的文件导入蓝图对象的下面
from . import views
