from app.db import db
from datetime import datetime

class HelloModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(140), index=True)
    time = db.Column(db.String(140), index=True)

    def __init__(self, message, time=datetime.time(datetime.now())):
        self.message = message
        self.time = str(time)

    def json(self):
        return {
            "message": self.message,
            "time": self.time,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    

