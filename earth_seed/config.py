import os
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/earth_seed'

CSRF_ENABLED = True 
SECRET_KEY = 'big-secret'