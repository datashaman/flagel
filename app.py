import os
import json
import peewee

from bottle import run, get, view, template, static_file, request, debug, default_app, TEMPLATE_PATH

from config import config, APP_ROOT


TEMPLATE_PATH.append(os.path.join(APP_ROOT, 'views'))

@get('/')
@view('root')
def root():
    return {}

# Static file catch-all route
@get('/<filename:path>')
def static_files(filename):
    return static_file(filename, root='%s/%s' % (APP_ROOT, config['static']))
