import app

from bottle import debug, default_app
from config import config


debug(config['debug'])
application = default_app()
