from flask_script import Manager, Server
from app import app, db, Rank


manager = Manager(app)
manager.add_command('server', Server())


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Rank=Rank)


if __name__ == '__main__':
    manager.run()
