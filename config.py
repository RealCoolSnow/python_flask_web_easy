class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xiaofengMUmu@0927@127.0.0.1:3306/snow?charset=utf8'
    WX_APPID = ""
    WX_SECRET = ""


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
