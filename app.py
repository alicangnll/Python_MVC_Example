# Uygulamanın başlatıcısı
# Uygulama bu dosyadan başlayacak
from flask import Flask
from flask_migrate import Migrate
from models.DBModel import db
from routes.Route import pclist

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(pclist)

if __name__ == '__main__':
    app.debug = True
    app.run()
