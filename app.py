#!/usr/bin/env python

import json
import peewee

from bottle import run, get, template, static_file, request

from models import Number

# Number.drop_table()

if not Number.table_exists():
    Number.create_table()

    numbers = (
        ('One', 1),
        ('Two', 2),
        ('Three', 3),
        ('Four', 4),
        ('Five', 5),
        ('Six', 6),
        ('Seven', 7),
        ('Eight', 8),
        ('Nine', 9),
        ('Ten', 10),
        ('Eleven', 11),
        ('Twelve', 12),
    )

    for label, sequence in numbers:
        number = Number.create(sequence=sequence,
                      label=label)

SHORT_POINT = 5
LONG_POINT = 9

def render_select(legend, name, options, multiple=False, **kwargs):
    kwargs['name'] = name
    kwargs['options'] = [option for option in options]
    kwargs['multiple'] = multiple

    format = kwargs.pop('format', default_format(kwargs['options'], multiple))

    if 'id' not in kwargs:
        kwargs['id'] = idify_name(name)

    return template('element.tpl', legend=legend, element=template('%s.tpl' % format, **kwargs))

def default_format(options, multiple=False):
    len_options = len(options)

    if len_options == 1:
        format = 'checkbox'
    elif len_options <= SHORT_POINT:
        if multiple:
            format = 'checkbox-group'
        else:
            format = 'radio-group'
    elif len_options <= LONG_POINT:
        format = 'select'
    else:
        if multiple:
            format = 'autocomplete-list'
        else:
            format = 'autocomplete'

    return format

def idify_name(name):
    return name

@get('/')
def root():
    numbers = Number.select().order_by(Number.sequence)

    elements = [
        render_select('Single', 'numbers', numbers.limit(1)),
        render_select('Single short', 'numbers', numbers.limit(SHORT_POINT)),
        render_select('Multiple short', 'numbers', numbers.limit(SHORT_POINT), multiple=True),
        render_select('Single medium', 'numbers', numbers.limit(LONG_POINT)),
        render_select('Multiple medium', 'numbers', numbers.limit(LONG_POINT), multiple=True),
        render_select('Single long', 'numbers', numbers),
        render_select('Multiple long', 'numbers', numbers, multiple=True),
    ]

    return template('page.tpl', content=''.join(elements))

@get('/ajax')
def ajax():
    q = request.params.q.lower()
    base = Number.select().where(peewee.fn.Lower(Number.label) % ('%s*' % q))
    count = base.count()

    page = int(request.params.get('page', 1))
    limit = int(request.params.get('per', SHORT_POINT))

    numbers = base.paginate(page, limit)

    return json.dumps({
        'more': count > (page * limit),
        'results': [{ 'id': number.id, 'text': number.label } for number in numbers]
    })

@get('/styles/<filename:path>')
def styles(filename):
    return static_file(filename, root='static/styles')

@get('/scripts/<filename:path>')
def scripts(filename):
    return static_file(filename, root='static/scripts')

@get('/plugins/<filename:path>')
def plugins(filename):
    return static_file(filename, root='static/plugins')

run(reloader=True)
