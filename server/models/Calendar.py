from .db import db


class Calendar(db.Model):
    __tablename__ = "calendar"

    c_id = db.Column(db.Integer, primary_key=True)
    c_start_date = db.Column(db.Date, nullable=False)
    c_end_date = db.Column(db.Date, nullable=False)

    def json(self):
        return {
            "c_id": self.c_id,
            "c_start_date": self.c_start_date.__str__(),
            "c_end_date": self.c_end_date.__str__()
        }