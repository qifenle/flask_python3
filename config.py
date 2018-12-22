# 导入redis
from redis import StrictRedis

class Config():
    DEBUG = None
    SECRET_KEY = 'mfbLEofXEGaMrUeKb88TsEslrHL/4G+mJtvI5AdyaUGVSHcviqkzJg=='
    # 指定session信息存储的位置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host='127.0.0.1',port=6379)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 88888
    # 配置数据库的连接和动态跟踪修改
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 定义开发模式
class DevelopmentConfig(Config):
    DEBUG = True

# 定义生产模式
class ProductionConfig(Config):
    DEBUG = False


config_dict = {
    'dev':DevelopmentConfig,
    'pro':ProductionConfig
}