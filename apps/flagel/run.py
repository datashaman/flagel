import os
import sys
from bottle import debug, run

# Add root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from apps import config
import routes


CONFIG = config.load_config('flagel')

DEBUG = CONFIG['debug']
debug(DEBUG)
run(reloader=DEBUG)
