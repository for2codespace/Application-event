from .db import db


class StaffList(db.Model):
    __tablename__ = "STAFF_LIST"

    SL_ID = db.Column(db.Integer, primary_key=True)
    SL_FIRSTNAME = db.Column(db.String(50), nullable=False)
    SL_SURNAME = db.Column(db.String(50), nullable=False)
    SL_LASTNAME = db.Column(db.String(50), nullable=False)
    SL_DIVISION_ID = db.Column(db.Integer, db.ForeignKey('DIVISION_LIST.DL_ID'), nullable=False)
    SL_IS_WORKS = db.Column(db.Boolean, nullable=False)

    def json(self):
        return {
            "SL_ID": self.SL_ID,
            "SL_FIRSTNAME": self.SL_FIRSTNAME,
            "SL_SURNAME": self.SL_SURNAME,
            "SL_LASTNAME": self.SL_LASTNAME,
            "SL_DIVISION_ID": self.SL_DIVISION_ID,
            "SL_IS_WORKS": self.SL_IS_WORKS
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()