import os
import yaml


def asbool(value):
    return value.lower() == 'true' or value.lower() == '1'

APP_ENV = os.getenv('APP_ENV', 'development')

config_filepath = os.path.join(os.path.dirname(__file__), 'config.yaml')
config = None

with open(config_filepath, 'r') as file:
    config = yaml.load(file)[APP_ENV]
