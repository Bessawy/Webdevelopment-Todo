from app import db
import enum
from sqlalchemy import Enum

class Status(enum.Enum):
    NotStarted = 'NotStarted'
    OnGoing = 'OnGoing'
    Completed = 'Completed'

def getStatus(value):
    if(value == 'NS'):
        return Status.NotStarted
    elif(value == 'OG'):
        return Status.OnGoing
    elif(value == 'CP'):
        return Status.Completed
    else:
        return None

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(100))
    acc_created = db.Column(db.String(80))
    last_updated = db.Column(db.String(80))

    def __repr__(self):
        return f'<emial: {self.email}>'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer)
    created = db.Column(db.String(80))
    last_updated = db.Column(db.String(80))
    status = db.Column(db.Enum(Status, values_callable=lambda x: [str(member.value) for member in Status]))
