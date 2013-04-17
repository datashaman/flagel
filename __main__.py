import app

from bottle import debug, run
from config import config


DEBUG = config['debug']
debug(DEBUG)
run(reloader=DEBUG)
