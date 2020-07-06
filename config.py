import os
base = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "thisismysecretkey"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///"+os.path.join(base, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False 