from .db import db


class Involvement(db.Model):
    __tablename__ = "involvement"

    i_id = db.Column(db.Integer, primary_key=True)
    i_event_id = db.Column(db.Integer, nullable=False)
    i_student_id = db.Column(db.Integer, db.ForeignKey('student.s_id'), nullable=False)

    def json(self):
        return {
            "i_id": self.i_id,
            "i_event_id": self.i_event_id,
            "i_student_id": self.i_student_id
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()
