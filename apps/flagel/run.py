import os
import sys
from bottle import debug, run, app

# Add root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from apps import config
import routes

CONFIG = config.load('flagel')

DEBUG = CONFIG['debug']
debug(DEBUG)

from beaker.middleware import SessionMiddleware
session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': os.path.join(config.ROOT, 'data'),
        'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

run(app=app, reloader=DEBUG)
