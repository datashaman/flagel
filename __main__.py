import os
import sys

from bottle import debug, run

from config import config
import app


DEBUG = config['debug']
debug(DEBUG)
run(reloader=DEBUG)
