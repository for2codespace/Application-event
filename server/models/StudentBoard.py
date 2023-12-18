from .db import db


class StudentBoard(db.Model):
    __tablename__ = "STUDENT_BOARD"

    SB_BOARD_ID = db.Column(db.Integer, primary_key=True)
    SB_CALENDAR_ID = db.Column(db.Integer, db.ForeignKey('CALENDAR.C_ID'), nullable=False)
    SB_STUDENT_ID = db.Column(db.Integer, db.ForeignKey('STUDENT.S_ID'), nullable=False)
    SB_POSITION_ID = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            "SB_BOARD_ID": self.SB_BOARD_ID,
            "SB_CALENDAR_ID": self.SB_CALENDAR_ID,
            "SB_STUDENT_ID": self.SB_STUDENT_ID,
            "SB_POSITION_ID": self.SB_POSITION_ID
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()
