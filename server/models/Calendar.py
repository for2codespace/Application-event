from datetime import date
from .db import db


class Calendar(db.Model):
    __tablename__ = "calendar"

    c_id = db.Column(db.Integer, primary_key=True)
    _start_date = db.Column(db.Date, nullable=False)
    _end_date = db.Column(db.Date, nullable=False)

    def json(self):
        return {
            "c_id": self.c_id,
            "c_start_date": self.c_start_date,
            "c_end_date": self.c_end_date
        }

    @property
    def c_start_date(self):
        return self._start_date.strftime("%Y-%m-%d")

    @c_start_date.setter
    def c_start_date(self, start_date: date):
        self._start_date = start_date

    @property
    def c_end_date(self):
        return self._end_date.strftime("%Y-%m-%d")

    @c_end_date.setter
    def c_end_date(self, end_date: date):
        self._end_date = end_date