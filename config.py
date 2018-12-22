# 导入redis
from redis import StrictRedis


class Config:
    DEBUG = None
    # 配置密钥
    SECRET_KEY = '8RliMjy2/jPnzFwFcieYuUTa+vHgqPKHjfmXZEUmGQXVcGHywnGY7g=='
    # 指定session信息储存的位置
    SESSION_TYPE = 'redis'
    SESSIOM_REDIS = StrictRedis(host='127.0.0.1',port=6379)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400
    # 配置数据库连接和动态追踪修改
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/info20'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 配置开发模式


class DevelopmentConfig(Config):
    DEBUG = True


# 配置生产模式


class ProductionConfig(Config):
    DEBUG = False


config_dict = {
    'dev':DevelopmentConfig,
    'pro':ProductionConfig
}