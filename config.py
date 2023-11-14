"""Flask APP configuration."""
from os import environ, path
from dotenv import load_dotenv


# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


# General Config
class Config:
    """Set Flask config variables."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")
    SECRET_KEY = environ.get("SECRET_KEY")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    URL = environ.get("URL")