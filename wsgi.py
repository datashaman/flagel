import os
from bottle import debug, default_app

from config import config
import app


debug(config['debug'])
application = default_app()
