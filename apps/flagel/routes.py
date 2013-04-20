import os
from bottle import get, view, static_file, TEMPLATE_PATH
from apps import config


CONFIG = config.load('flagel')
APP_ROOT = config.app_root('flagel')
TEMPLATE_PATH.append(os.path.join(APP_ROOT, 'views'))

@get('/')
@view('home')
def home():
    return {}

@get('/about')
@view('page')
def page():
    return {}

# Static file catch-all route
@get('/<filename:path>')
def static_files(filename):
    root = '%s/%s' % (config.ROOT, CONFIG['static'])
    return static_file(filename, root=root)
