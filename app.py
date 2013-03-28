from bottle import run, get, template, static_file

l = (
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

SHORT_POINT = 5
LONG_POINT = 9

def render(legend, name, options, multiple=False, **kwargs):
    kwargs['name'] = name
    kwargs['options'] = options
    kwargs['multiple'] = multiple
    format = kwargs.pop('format', default_format(options, multiple))
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
    elements = [
        render('Single', 'numbers', [l[0]]),
        render('Single short', 'numbers', l[:SHORT_POINT]),
        render('Multiple short', 'numbers', l[:SHORT_POINT], multiple=True),
        render('Single medium', 'numbers', l[:LONG_POINT]),
        render('Multiple medium', 'numbers', l[:LONG_POINT], multiple=True),
        render('Single long', 'numbers', l),
        render('Multiple long', 'numbers', l, multiple=True),
    ]

    return template('page.tpl', content=''.join(elements))

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
