from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_seeder import FlaskSeeder

app = Flask(__name__, template_folder='views')
app.config.from_object(Config)
api = Api(app, prefix='/api')
web = Api(app) 
db = SQLAlchemy(app)
migrate = Migrate(app, db)
seeder = FlaskSeeder()
seeder.init_app(app, db)

from app import routes
from app import models
