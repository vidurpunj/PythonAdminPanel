# __init__.py
import pymysql

pymysql.install_as_MySQLdb()

from django.conf import settings

# Check if the DATABASES setting is defined in settings.py
if hasattr(settings, 'DATABASES'):
    DATABASES = settings.DATABASES
else:
    # Define default database configuration if DATABASES is not defined
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'python_admin_panel',
            'USER': 'root',
            'PASSWORD': 'Punj@1234',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

# Additional database setup code if needed
