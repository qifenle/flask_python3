from flask import Flask
# 导入数据库扩展
from flask_sqlalchemy import SQLAlchemy
# 导入flask_session扩展包
from flask_session import Session
# 导入配置文件
from config import config_dict


# 实例化sql对象
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    # 使用配置对象
    app.config.from_object(config_dict[config_name])
    # 通过函数让db和app进行关联
    db.init_app(app)
    # Session初始化对象
    Session(app)
    # 导入蓝图 注册蓝图
    from info.modules.index import index_blue
    app.register_blueprint(index_blue)
    return app