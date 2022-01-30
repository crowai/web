import os

from flask import Flask

from crow.extensions import (
  db,
  bcrypt,
  login_manager
)

def create_app(config_filename="flask.cfg"):
  """Create Flask application factories."""

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_pyfile(config_filename)

  initialize_extensions(app)
  register_blueprints(app)

  return app

def initialize_extensions(app):
  """Initializing Flask extensions."""

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)

  login_manager.login_view = "auth.login"

  return None

def register_blueprints(app):
  """Registering Flask blueprints."""

  from crow.main.views import main
  from crow.user.public.views import user
  from crow.user.auth.views import auth
  from crow.admin.views import admin

  app.register_blueprint(main)
  app.register_blueprint(user)
  app.register_blueprint(auth)
  app.register_blueprint(admin)
  
  return None