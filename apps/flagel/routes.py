import os
import json
import requests
from bottle import get, post, view, request, static_file, TEMPLATE_PATH, abort
from apps import config


CONFIG = config.load('flagel')
APP_ROOT = config.app_root('flagel')
TEMPLATE_PATH.append(os.path.join(APP_ROOT, 'views'))

@get('/')
@view('home')
def home():
    return {}

@get('/auth/status')
def status():
    session = request.environ.get('beaker.session')
    return dict(email=session.get('email'))

@post('/auth/login')
def login():
    # The request has to have an assertion for us to verify
    if 'assertion' not in request.forms:
        abort(400)

    # Send the assertion to Mozilla's verifier service.
    assertion = request.forms.get('assertion')

    # audience = '%s://%s' % (request.urlparts.scheme, request.urlparts.netloc)
    audience = 'http://localhost:8080'

    data = dict(assertion=assertion, audience=audience)
    resp = requests.post('https://verifier.login.persona.org/verify', data=data, verify=True)

    # Did the verifier respond?
    if resp.ok:
        # Parse the response
        verification_data = json.loads(resp.content)

        # Check if the assertion was valid
        if verification_data['status'] == 'okay':
            # Log the user in by setting a secure session cookie
            session = request.environ.get('beaker.session')
            session['email'] = verification_data['email']
            session.save()
            return dict(email=session['email'])

    # Oops, something failed. Abort.
    abort(500)

@post('/auth/logout')
def logout():
    # Log the user out by deleting the session
    session = request.environ.get('beaker.session')
    session.delete()

# Static file catch-all route
@get('/<filename:path>')
def static_files(filename):
    root = '%s/%s' % (config.ROOT, CONFIG['static'])
    return static_file(filename, root=root)
