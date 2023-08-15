from pathlib import Path

#settings.pyからそのままコピー
SECRET_KEY = '7b$o)ja+)q)0s(mn!ma3kgq+w#o1=qp5)_+5h!+p@g!g0t3xah'

BASE_DIR = Path(__file__).resolve().parent.parent

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django.db.backends.mysql',
    }
}

DEBUG = True #ローカルでDebugできるようになります。