import os
import yaml


APP_ENV = os.getenv('APP_ENV', 'development')
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def load(app_name):
    config_filepath = os.path.join(ROOT, 'config', '%s.yaml' % app_name)
    config = None

    with open(config_filepath, 'r') as file:
        config = yaml.load(file)[APP_ENV]

    return config

def app_root(app_name):
    return os.path.join(ROOT, 'apps', app_name)
