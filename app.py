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
    # ('Ten', 10),
    # ('Eleven', 11),
    # ('Twelve', 12),
)

def render(name, options, multiple=False, **kwargs):
    kwargs['name'] = name
    kwargs['options'] = options
    format = kwargs.pop('format', default_format(options, multiple))
    if 'id' not in kwargs:
        kwargs['id'] = idify_name(name)
    return template('%s.tpl' % format, **kwargs)

def default_format(options, multiple=False):
    len_options = len(options)

    if len_options == 1:
        format = 'checkbox'
    elif len_options <= 10:
        if multiple:
            format = 'checkbox-group'
        else:
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
    return template('page.tpl', content=render('numbers', l, multiple=True))

@get('/styles/<filename:path>')
def styles(filename):
    return static_file(filename, root='static/styles')

@get('/scripts/<filename:path>')
def scripts(filename):
    return static_file(filename, root='static/scripts')

run(reloader=True)
