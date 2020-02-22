# django_app

## System Environment

- Python 3

## Run

```
~/.bashrc
 alias python='/usr/bin/python3’

$ npm install
$ apt install python3-pip
$ python -m pip install --upgrade pip
$ pip3 install django
$ pip3 install stripe
$ pip3 install django-sslserver
$ python manage.py runserver 0.0.0.0:<port>

```

## Djangoの使い方

■Djangoプロジェクト作成
```
django-admin startproject プロジェクト名
```

■Djangoアプリケーション作成
```
python manage.py startapp アプリケーション名
```

■manage.py
```
Djangプロジェクトを実行する様々な機能に関するプログラム
```

■__init__.py
```
Djangプロジェクトを実行するときの初期化処理を行うスクリプトファイル
```

■settings.py
```
プロジェクトの設定情報を記述したファイル
アプリケーションを新規作成した際はこのファイルにも追記する。
```

■urls.py
```
プロジェクトで使用するURLを管理するファイル
```

■wsgi.py
```
Webアプリのメインプログラム部分
```



