from bottle import get, view, static_file
from config import config, APP_ROOT

@get('/')
@view('root')
def root():
    return {}

# Static file catch-all route
@get('/<filename:path>')
def static_files(filename):
    return static_file(filename, root='%s/%s' % (APP_ROOT, config['static']))
