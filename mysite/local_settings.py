from pathlib import Path

#settings.pyからそのままコピー
SECRET_KEY = '***************************'

BASE_DIR = Path(__file__).resolve().parent.parent

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django.db.backends.mysql',
    }
}

DEBUG = True #ローカルでDebugできるようになります。