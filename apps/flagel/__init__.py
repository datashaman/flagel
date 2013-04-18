import os
from bottle import TEMPLATE_PATH

from apps import config
APP_ROOT = config.app_root('flagel')

# Add the views directory to template path, since we cannot be
# sure of our current working directory
