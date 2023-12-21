from .db import db


class StudyType(db.Model):
    __tablename__ = "study_type"

    st_id = db.Column(db.Integer, primary_key=True)
    st_type = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            "st_id": self.st_id,
            "st_type": self.st_type
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()
