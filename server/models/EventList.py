from .db import db, BaseModel
from datetime import date


class EventList(BaseModel):
    __tablename__ = "event_list"

    el_id = db.Column(db.Integer, primary_key=True)
    el_c_start_date = db.Column(db.Date)
    el_c_end_date = db.Column(db.Date)
    el_group_id = db.Column(db.Integer, db.ForeignKey('group_list.gl_id'), nullable=False)
    el_student_id = db.Column(db.Integer, db.ForeignKey('student.s_id'), nullable=False)
    el_staff_id = db.Column(db.Integer, db.ForeignKey('staff_list.sl_id'), nullable=False)
    el_ec_id = db.Column(db.Integer, db.ForeignKey('event_card.ec_id'), nullable=False)

    def json(self):
        return {
            "el_id": self.el_id,
            "el_c_start_date": self.el_c_start_date.strftime("%Y-%m-%d"),
            "el_c_end_date": self.el_c_end_date.strftime("%Y-%m-%d"),
            "el_group_id": self.el_group_id,
            "el_student_id": self.el_student_id,
            "el_staff_id": self.el_staff_id,
            "el_ec_id": self.el_ec_id
        }

    @classmethod
    def get_by_range(cls, date_from: date, date_to: date):
        return cls.query.filter(
            cls.el_c_start_date.between(date_from, date_to) &
            cls.el_c_end_date.between(date_from, date_to)
        ).all()

    @classmethod
    def get_by_ec_id(cls, ec_id: int):
        return cls.query.filter(
            cls.el_ec_id == ec_id
        ).first()