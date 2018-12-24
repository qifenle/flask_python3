
# 导入管理器
from flask_script import Manager
# 导入迁移框架
from flask_migrate import Migrate,MigrateCommand
# 导入app,db，配置文件
from info import create_app,db,models

app = create_app('dev')

# 实例化管理器对象
manager = Manager(app)
# 使用迁移框架
Migrate(app,db)
# 添加迁移命令
manager.add_command('db',MigrateCommand)




if __name__ == '__main__':
    print(app.url_map)
    manager.run()