import os
from subprocess import call

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