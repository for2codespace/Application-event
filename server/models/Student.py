from .db import db


class Student(db.Model):
    __tablename__ = "STUDENT"

    S_ID = db.Column(db.Integer, primary_key=True)
    S_FIRSTNAME = db.Column(db.String(50), nullable=False)
    S_SURNAME = db.Column(db.String(50), nullable=False)
    S_LASTNAME = db.Column(db.String(50), nullable=False)
    S_GROUP_ID = db.Column(db.Integer, db.ForeignKey('GROUP_LIST.GL_ID'), nullable=False)
    S_STUDY_ID = db.Column(db.Integer, db.ForeignKey('STUDY_TYPE.ST_ID'), nullable=False)

    def json(self):
        return {
            "S_ID": self.S_ID,
            "S_FIRSTNAME": self.S_FIRSTNAME,
            "S_SURNAME": self.S_SURNAME,
            "S_LASTNAME": self.S_LASTNAME,
            "S_GROUP_ID": self.S_GROUP_ID,
            "S_STUDY_ID": self.S_STUDY_ID
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
