import os

from bottle import get, view, static_file, TEMPLATE_PATH
from config import config, APP_ROOT


# Add the views directory to template path, since we cannot be
# sure of our current working directory
TEMPLATE_PATH.append(os.path.join(APP_ROOT, 'views'))

@get('/')
@view('root')
def root():
    return {}

# Static file catch-all route
@get('/<filename:path>')
def static_files(filename):
    return static_file(filename, root='%s/%s' % (APP_ROOT, config['static']))
