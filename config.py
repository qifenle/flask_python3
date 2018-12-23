# 导入redis
from redis import StrictRedis


class Config:
    DEBUG = None
    # 配置密钥
    SECRET_KEY = 'tKoYO4p+G83JW5qnzVaTOzK/UV3QxD62y4rjbpF6LmxxIpgFjWOydA=='
    # 指定session信息存储的位置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host='127.0.0.1', port=6379)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400
    # 配置数据库的连接和追踪修改
    SQLALCHEMY_DATABASE_URI= 'mysql://root:mysql@localhost/info20'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 配置开发模式

class DevelopmentConfig(Config):
    DEBUG = True

# 配置生产模式


class ProductionConfig(Config):
    DEBUG = False


# 定义配置模式字典
config_dict = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig
}