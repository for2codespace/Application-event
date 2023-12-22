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
            "s_id": self.s_id,
            "s_firstname": self.s_firstname,
            "s_surname": self.s_surname,
            "s_lastname": self.s_lastname,
            "s_group_id": self.s_group_id,
            "s_study_type_id": self.s_study_type_id
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
