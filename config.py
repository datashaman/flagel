import os
import yaml


def asbool(value):
    return value.lower() == 'true' or value.lower() == '1'

APP_ENV = os.getenv('APP_ENV', 'development')
APP_ROOT = os.path.abspath(os.path.dirname(__file__))

config_filepath = os.path.join(APP_ROOT, 'config.yaml')
config = None

with open(config_filepath, 'r') as file:
    config = yaml.load(file)[APP_ENV]
