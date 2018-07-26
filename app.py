from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from dao.model import TodoList, ModifiedDate
from dao.model import db

from core.api import core_blueprint

from config import DevConfig

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DevConfig.FLASK_DATALAYER

db.init_app(app)
migrate = Migrate(app, db)

cors = CORS(app, origins="*", allow_headers=[
    "Content-Type",
    "Authorization",
    "Accept",
    "Content-Type",
    "Access-Control-Allow-Credentials",
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Origin",
],
            supports_credentials=True)

app.register_blueprint(core_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run()
