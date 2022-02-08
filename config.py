import os
from subprocess import call

basedir = os.path.abspath(os.path.dirname(__file__))

# Here we are using a class to store configuration variables.
# As the application needs more configurations items, they can be added to this class 
# Later if I find that I need more than onconfiguration set, I can create subclasses of this

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

# The value of the SECRET_KEY is set as an expression with two terms, joined by the 'or' operator 
# The first term looks for the value of an environment variable, also called SECRET_KEY
# The second term is just a hardcoded string
# AKA the value sources from an environment variable is perferred but if the env doesn't define
# that variable, then the string is iused instead 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
# The SQLALCHEMY_TRACK_MODIFICATIONS configuration option is set to False 
# to disable a feature of Flask-SQLAlchemy that I do not need, 
# which is to send a signal to the application every time a change is about to be made in the database.