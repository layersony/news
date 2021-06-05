from app import news_app
from flask_script import Manager, Server

app = news_app('development')

manager = Manager(app)
manager.add_command('server', Server)


if __name__ == '__main__':
  manager.run()