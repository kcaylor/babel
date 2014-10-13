#!/usr/bin/python
import os
COV = None
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
def test(coverage=False):
    """Run the unit tests (using nose)"""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        print('Restarting script...')
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import nose
    if COV:
        print('Ending coverage')
        COV.stop()
        COV.save()
        print('Coverage Summary')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML Version: file://%s/index.html' % covdir)
        COV.erase()
    nose.main(argv=[''])

@manager.command
def serve():
    from waitress import serve
    port = int(os.getenv('PORT') or 5000)
    serve(app, port=port)

if __name__ == '__main__':
    manager.run()

