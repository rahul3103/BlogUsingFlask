from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()

#Flask-Bootstrap is imported from the flask.ext namespace and initialized by passing the application instance in the constructor.

mail = Mail()
moment = Moment()

#Flask-Moment depends on jquery.js in addition to moment.js. These two libraries need to be included somewhere in the HTML document—either directly, in which case you can choose what versions to use, or through the helper functions provided by the extension, which reference tested versions of these libraries from a Content Delivery Network(CDN). Because Bootstrap already includes jquery.js, only moment.js needs to be added in this case.

db = SQLAlchemy()

#The db object instantiated from class SQLAlchemy represents the database and provides access to all the functionality of Flask-SQLAlchemy.

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])

#The configuration settings stored in one of the classes defined in config.py can be imported directly into the application using the from_object() method available in Flask’s app.config configuration object. The configuration object is selected by name from the config dictionary. Once an application is created and configured, the extensions can be initialized.

	config[config_name].init_app(app)
	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)

#Calling init_app() on the extensions that were created earlier completes their initialization.

# attach routes and custom error pages here

	return app