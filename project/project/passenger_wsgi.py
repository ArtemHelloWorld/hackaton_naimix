import os, sys
site_user_root_dir = '/home/a/artemk19/artemk19.beget.tech/public_html'
sys.path.insert(0, site_user_root_dir + '/project')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
