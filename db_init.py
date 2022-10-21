from app import app, db
from app.models import User, Todo

with app.app_context():
    db.create_all()


