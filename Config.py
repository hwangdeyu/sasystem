class Config(object):
    ACCOUNT = 'admin'
    PASSWORD = 'xunfeng321'


class ProductionConfig(Config):
    DB = '127.0.0.1'
    PORT = 65521
    DBUSERNAME = 'scan'
    DBPASSWORD = 'your password'#'scanlol66'
    DBNAME = 'xunfeng'
	
	#test