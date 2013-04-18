import app

from bottle import debug, default_app
from apps import load_config


CONFIG = load_config('flagel')

debug(CONFIG['debug'])
application = default_app()
