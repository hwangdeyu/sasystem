class Config(object):
    ACCOUNT = 'buptnerd'
    PASSWORD = 'bupt'


class ProductionConfig(Config):
    DB = '127.0.0.1'
    PORT = 65521
    DBUSERNAME = 'scan'
    DBPASSWORD = 'buptnerd'
    DBNAME = 'xunfeng'
