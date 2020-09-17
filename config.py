'''
Description: 
Author: CoolSnow (coolsnow2020@gmail.com)
Date: 2020-09-17 10:49:40
LastEditors: CoolSnow
LastEditTime: 2020-09-17 16:18:01
'''
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/snow?charset=utf8'
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
