import os
basedir = os.path.abspath(os.path.dirname(__file__))

"""
print os.path.abspath(__file__) : C:\Users\e2sn7cy\Documents\GitHub\BlogUsingFlask\config.py
print os.path.dirname(__file__) : {empty}
print basedir : C:\Users\e2sn7cy\Documents\GitHub\BlogUsingFlask

os.path.abspath(path) : Return a normalized absolutized version of the pathname path. On most platforms, this is equivalent to calling the function normpath()

os.path.dirname(path) : Return the directory name of pathname path. This is the first element of the pair returned by passing path to the function split().

"""

class config:
	SECRET_KEY = os.environ.get('SECRET_KEY')

#The value of the SECRET_KEY, due to its sensitive nature, can be set in the environment, but a default value is provided in case the environment does not define it.

	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

#The configuration key SQLALCHEMY_COMMIT_ON_TEARDOWN, which can be set to True to enable automatic commits of database changes at the end of each request.

	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

#The SQLALCHEMY_DATABASE_URI variable is assigned different values under each of the three configurations. This enables the application to run under different configurations, each using a different database.


class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}


