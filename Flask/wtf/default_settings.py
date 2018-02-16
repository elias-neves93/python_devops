class BaseConfig(object):
    DEBUG = False


class ProductionConfig(BaseConfig):
    SECRET_KEY = "djfnsdjkfnsjdf"
    MEDIA_ROOT = "/path/to/media_files/in/server"


class DevelopmentConfig(ProductionConfig):
    MEDIA_ROOT = "/home/me/projects/wtf/media_files"
