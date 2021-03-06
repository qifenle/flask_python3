from flask import Flask
# 导入数据库扩展包
from flask_sqlalchemy import SQLAlchemy
# 导入扩展包flask_session
from flask_session import Session
# 导入配置文件
from config import config_dict,Config
# 导入标准日志模块
import logging
from logging.handlers import RotatingFileHandler

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG) # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("flask_python_stage/flask/logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)

from redis import StrictRedis
redis_store = StrictRedis(host=Config.SESSION_HOST,port=Config.SESSION_PORT)

# 实例化数据库对象
db = SQLAlchemy()
# 定义函数 生产不同的app对象
def create_app(config_name):
    app = Flask(__name__)
    # 使用配置对象
    app.config.from_object(config_dict[config_name])
    # 使用函数把app和db关联
    db.init_app(app)
    # Session初始化
    Session(app)
    from info.modules.index import index_blue
    app.register_blueprint(index_blue)
    from info.modules.passport import passport_blue
    app.register_blueprint(passport_blue)
    return app