from .db import db


class Calendar(db.Model):
    __tablename__ = "CALENDAR"

    C_ID = db.Column(db.Integer, primary_key=True)
    C_START_DATE = db.Column(db.Date, nullable=False)
    C_END_DATE = db.Column(db.Date, nullable=False)

    def json(self):
        return {
            "C_ID": self.C_ID,
            "C_START_DATE": self.C_START_DATE,
            "C_END_DATE": self.C_END_DATE
        }