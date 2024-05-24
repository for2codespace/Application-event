from .db import db, BaseModel


class Involvement(BaseModel):
    __tablename__ = "involvement"

    i_id = db.Column(db.Integer, primary_key=True)
    i_event_id = db.Column(db.Integer, db.ForeignKey('event_list.el_id'), nullable=False)
    i_student_id = db.Column(db.Integer, db.ForeignKey('student.s_id'), nullable=False)

    def json(self):
        return {
            "i_id": self.i_id,
            "i_event_id": self.i_event_id,
            "i_student_id": self.i_student_id
        }
