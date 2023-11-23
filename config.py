import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'passwrd'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	POSTS_PER_PAGE = 3
	MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25) or 587
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'foxxxique@gmail.com'
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'pcrtiazbioatwwpf'
	ADMINS = ['foxxxique@gmail.com']
	LANGUAGES = ['en', 'es']