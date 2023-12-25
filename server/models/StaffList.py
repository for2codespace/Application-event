from .db import db


class StaffList(db.Model):
    __tablename__ = "staff_list"

    sl_id = db.Column(db.Integer, primary_key=True)
    sl_firstname = db.Column(db.String(50), nullable=False)
    sl_surname = db.Column(db.String(50), nullable=False)
    sl_lastname = db.Column(db.String(50), nullable=False)
    sl_division_id = db.Column(db.Integer, db.ForeignKey('division.dl_id'), nullable=False)
    sl_is_works = db.Column(db.Boolean, nullable=False)

    def json(self):
        return {
            "sl_id": self.sl_id,
            "sl_firstname": self.sl_firstname,
            "sl_surname": self.sl_surname,
            "sl_lastname": self.sl_lastname,
            "sl_division_id": self.sl_division_id,
            "sl_is_works": "работает" if self.sl_is_works else "не работает"
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()