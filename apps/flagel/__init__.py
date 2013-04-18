import os

from bottle import TEMPLATE_PATH
from config import APP_ROOT

# Add the views directory to template path, since we cannot be
# sure of our current working directory
TEMPLATE_PATH.append(os.path.join(APP_ROOT, 'app', 'views'))

import routes
