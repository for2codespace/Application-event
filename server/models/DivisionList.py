from .db import db


class DivisionList(db.Model):
    __tablename__ = "DIVISION_LIST"

    DL_ID = db.Column(db.Integer, primary_key=True)
    DL_NAME = db.Column(db.String(50), nullable=False)
    DL_PARENT_DIVISION_ID = db.Column(db.Integer)

    def json(self):
        return {
            "DL_ID": self.DL_ID,
            "DL_NAME": self.DL_NAME,
            "DL_PARENT_DIVISION_ID": self.DL_PARENT_DIVISION_ID
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()
