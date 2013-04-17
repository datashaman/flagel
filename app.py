import os
import json
import peewee

from models import Number
from bottle import run, get, template, static_file, request, debug, default_app, TEMPLATE_PATH

from config import config, APP_ROOT


TEMPLATE_PATH.append(os.path.join(APP_ROOT, 'views'))

SHORT_POINT = 5
LONG_POINT = 9

POINTS = (
    (1, 'checkbox'),
    (SHORT_POINT, 'checkbox-group', 'radio-group'),
    (LONG_POINT, 'select'),
    ('autocomplete-list', 'autocomplete'),
)

def label(text, content):
    return '<label>%s<br />%s</label>' % (text, content)

def select(name, options, multiple=False, **kwargs):
    kwargs['name'] = name
    kwargs['options'] = [option for option in options]
    kwargs['multiple'] = multiple

    format = kwargs.pop('format', default_format(kwargs['options'], multiple))

    if 'id' not in kwargs:
        kwargs['id'] = idify_name(name)

    return template('%s.tpl' % format, **kwargs)

def fieldset(legend, content):
    return template('fieldset.tpl', legend=legend, content=content)

def resolve_multiple(defn, multiple):
    if len(defn) == 1:
        return defn[0]
    else:
        return defn[0] if multiple else defn[1]

def default_format(options, multiple=False):
    len_options = len(options)
    len_points = len(POINTS)

    for index, defn in enumerate(POINTS):
        defn = list(defn)
        if index < len_points - 1:
            point = defn.pop(0)
            if len_options <= point:
                return resolve_multiple(defn, multiple)
        else:
            return resolve_multiple(defn, multiple)

    raise 'Should not happen'

def idify_name(name):
    return name

@get('/')
@view('root')
def root():
    numbers = Number.select().order_by(Number.sequence)

    select_elements = [
        fieldset('Single', select('numbers', numbers.limit(1))),
        fieldset('Single short', select('numbers', numbers.limit(SHORT_POINT))),
        fieldset('Multiple short', select('numbers', numbers.limit(SHORT_POINT), multiple=True)),
        fieldset('Single medium', select('numbers', numbers.limit(LONG_POINT))),
        fieldset('Multiple medium', select('numbers', numbers.limit(LONG_POINT), multiple=True)),
        fieldset('Single long', select('numbers', numbers)),
        fieldset('Multiple long', select('numbers', numbers, multiple=True)),
    ]

    return template('page.tpl', select_content=''.join(select_elements))

@get('/ajax')
def ajax():
    q = request.params.q.lower()
    base = Number.select().where(peewee.fn.Lower(Number.label) % ('%s*' % q)).order_by(Number.sequence)
    count = base.count()

    page = int(request.params.get('page', 1))
    limit = int(request.params.get('per', SHORT_POINT))

    if 'page' in request.params or 'per' in request.params:
        numbers = base.paginate(page, limit)
    else:
        numbers = base

    payload = {
        'results': [{ 'id': number.id, 'text': number.label } for number in numbers]
    }

    if 'page' in request.params or 'per' in request.params:
        payload['more'] = count > (page * limit)

    return json.dumps(payload)

def static_root(path=''):
    return '%s/%s/%s' % (APP_ROOT, config['static'], path)

for path in ['styles', 'scripts', 'plugins', 'components']:
    def func(path=path):
        get('/%s/<filename:path>' % path)(lambda filename: static_file(filename, root=static_root(path)))
    func()

# Static file catch-all route
@get('/<filename:path>')
def static_files(filename):
    return static_file(filename, root='%s/%s' % (APP_ROOT, config['static']))
