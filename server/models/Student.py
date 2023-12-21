from .db import db


class Student(db.Model):
    __tablename__ = "student"

    s_id = db.Column(db.Integer, primary_key=True)
    s_firstname = db.Column(db.String(50), nullable=False)
    s_surname = db.Column(db.String(50), nullable=False)
    s_lastname = db.Column(db.String(50), nullable=False)
    s_group_id = db.Column(db.Integer, nullable=False)
    s_study_type_id = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            "S_ID": self.s_id,
            "S_FIRSTNAME": self.s_firstname,
            "S_SURNAME": self.s_surname,
            "S_LASTNAME": self.s_lastname,
            "S_GROUP_ID": self.s_group_id,
            "S_STUDY_ID": self.s_study_type_id
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
