from .db import db


class Involvement(db.Model):
    __tablename__ = "INVOLVEMENT"

    I_ID = db.Column(db.Integer, primary_key=True)
    I_EVENT_ID = db.Column(db.Integer, nullable=False)
    I_STUDENT_ID = db.Column(db.Integer, db.ForeignKey('STUDENT.S_ID'), nullable=False)

    def json(self):
        return {
            "I_ID": self.I_ID,
            "I_EVENT_ID": self.I_EVENT_ID,
            "I_STUDENT_ID": self.I_STUDENT_ID
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()
