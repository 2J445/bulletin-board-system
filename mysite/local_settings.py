from pathlib import Path

#settings.pyからそのままコピー
SECRET_KEY = '7b$o)ja+)q)0s(mn!ma3kgq+w#o1=qp5)_+5h!+p@g!g0t3xah'

BASE_DIR = Path(__file__).resolve().parent.parent

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #Herokuのデータベースに関する設定
        
        #'ENGINE': 'django.db.backends.mysql', #mysqlをデータベースとして使用することを指定
        'NAME': 'mysite', #データベース名
        'USER': 'DBuser', #データベースを作成したユーザー名
        'PASSWORD': 'DBuser-24', #ログインするためのパスワード
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DEBUG = True #ローカルでDebugできるようになります。