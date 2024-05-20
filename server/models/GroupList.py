from .db import db
from datetime import date


class GroupList(db.Model):
    __tablename__ = "group_list"

    gl_id = db.Column(db.Integer, primary_key=True)
    gl_name = db.Column(db.Integer, nullable=False)
    _year = db.Column(db.Date, nullable=False)

    def json(self):
        return {
            "gl_id": self.gl_id,
            "gl_name": self.gl_name,
            "gl_year": self.gl_year
        }

    @property
    def gl_year(self) -> str:
        return self._year.strftime("%Y")

    @gl_year.setter
    def gl_year(self, date: date) -> None:
        self._year = date