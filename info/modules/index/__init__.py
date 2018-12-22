# 创建蓝图，使用蓝图，注册蓝图
from flask import Blueprint

index_blue = Blueprint('index_blue',__name__)

from . import views