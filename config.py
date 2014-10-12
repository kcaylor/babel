import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('APP_SECRET')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        "DB": os.environ.get('MONGODB_DEV_DATABASE'),
        "USERNAME": os.environ.get('MONGODB_DEV_USER'),
        "PASSWORD": os.environ.get('MONGODB_DEV_PASSWORD'),
        "HOST": os.environ.get('MONGODB_DEV_HOST'),
        "PORT": int(os.environ.get('MONGODB_DEV_PORT'))
    }

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

