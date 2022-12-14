from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
app.config.from_object('config.ConfigPostgres')
db = SQLAlchemy(app)

from app import views

