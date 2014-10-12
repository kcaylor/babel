#!/usr/bin/python
import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app
from app.models import db

from app.models import Dataset, Vic_Conus_3km
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

def make_shell_context():
    return dict(
        app=app,
        Dataset=Dataset,
        Vic_Conus_3km=Vic_Conus_3km,
        db=db,
    )

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def serve():
    from waitress import serve
    port = int(os.getenv('PORT') or 5000)
    serve(app, port=port)

if __name__ == '__main__':
    manager.run()

