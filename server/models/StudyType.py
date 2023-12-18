from .db import db


class StudyType(db.Model):
    __tablename__ = "STUDY_TYPE"

    ST_ID = db.Column(db.Integer, primary_key=True)
    ST_TYPE = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            "ST_ID": self.ST_ID,
            "ST_TYPE": self.ST_TYPE
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()
