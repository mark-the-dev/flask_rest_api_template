import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

"""
flask --app 'app/main:create_app("dev")' run
"""
class DevelopmentConfig(Config):
    ENV_NAME = "dev"

    # SQLAlchemy Config
    # DB_HOST = os.getenv("DEV_DB_HOST")
    # DB_USER = os.getenv("DEV_DB_USER")
    # DB_PASSWORD = os.getenv("DEV_DB_PASSWORD")
    # DB_DATABASE = os.getenv("DEV_DB_DATABASE")

"""
flask --app 'app/main:create_app("test")' run
"""
class TestingConfig(Config):
    ENV_NAME = "test"
    TESTING = True

    # SQLAlchemy Config
    # DB_HOST = os.getenv("DB_HOST")
    # DB_USER = os.getenv("DB_USER")
    # DB_PASSWORD = os.getenv("DB_PASSWORD")
    # DB_DATABASE = os.getenv("DB_DATABASE")

"""
flask --app 'app/main:create_app("prod")' run
"""
class ProductionConfig(Config):
    ENV_NAME = "prod"

    # SQLAlchemy Config
    # DB_HOST = os.getenv("PROD_DB_HOST")
    # DB_USER = os.getenv("PROD_DB_USER")
    # DB_PASSWORD = os.getenv("PROD_DB_PASSWORD")
    # DB_DATABASE = os.getenv("PROD_DB_DATABASE")

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY