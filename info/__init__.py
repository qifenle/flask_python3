from flask import Flask
# 导入扩展包 flask_session
from flask_session import Session
# 导入数据库扩展
from flask_sqlalchemy import SQLAlchemy
# 导入配置文件
from config import config_dict

# 实例化sqlchemy对象
db = SQLAlchemy()

# 定义函数，工厂函数，生产不同的app函数
def create_app(config_name):
    app = Flask(__name__)
    # 使用配置对象
    app.config.from_object(config_dict[config_name])
    # 通过函数让db和app进行关联
    db.init_app(app)
    # Session初始化
    Session(app)
    # 导入蓝图 注册蓝图
    from info.modules.index import index_blue
    app.register_blueprint(index_blue)

    return app