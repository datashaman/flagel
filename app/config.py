import os
import yaml


APP_ENV = os.getenv('APP_ENV', 'development')
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

config_filepath = os.path.join(APP_ROOT, 'config', 'config.yaml')
config = None

with open(config_filepath, 'r') as file:
    config = yaml.load(file)[APP_ENV]
