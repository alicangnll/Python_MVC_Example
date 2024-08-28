import os
SECRET_KEY = os.urandom(32)
# Uygulamanın ana dizini
basedir = os.path.abspath(os.path.dirname(__file__))
# Debug mod ayarı
DEBUG = True
# Veritaban bağlantısı
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(os.getcwd()) + "/instance/data.db"
# Flask-SQLAlchemy hatalarını ve debug loglarını gizleme veya gösterme ayarları
SQLALCHEMY_TRACK_MODIFICATIONS = False