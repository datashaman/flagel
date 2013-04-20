import app

from bottle import debug, default_app
from apps import config


CONFIG = config.load('flagel')

debug(CONFIG['debug'])
application = default_app()
