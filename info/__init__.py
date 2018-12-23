from flask import Flask
# 导入数据库扩展包
from flask_sqlalchemy import SQLAlchemy
# 导入扩展包flask_session
from flask_session import Session
# 导入配置文件
from config import config_dict

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
    return app