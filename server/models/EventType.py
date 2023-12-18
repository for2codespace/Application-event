from .db import db


class EventType(db.Model):
    __tablename__ = "EVENT_TYPE"

    ET_ID = db.Column(db.Integer, primary_key=True)
    ET_TYPE = db.Column(db.String(50), nullable=False)
    ET_CLASS = db.Column(db.Integer, nullable=False)
    ET_NAME = db.Column(db.String(50), nullable=False)
    ET_EVENT_DATE = db.Column(db.Date)
    ET_LOCATION = db.Column(db.String(50))
    ET_CALENDAR_ID = db.Column(db.Integer, db.ForeignKey('CALENDAR.C_ID'), nullable=False)

    def json(self):
        return {
            "ET_ID": self.ET_ID,
            "ET_TYPE": self.ET_TYPE,
            "ET_CLASS": self.ET_CLASS,
            "ET_NAME": self.ET_NAME,
            "ET_EVENT_DATE": self.ET_EVENT_DATE,
            "ET_LOCATION": self.ET_LOCATION,
            "ET_CALENDAR_ID": self.ET_CALENDAR_ID
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
