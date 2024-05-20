from .db import db
from datetime import date


class EventList(db.Model):
    __tablename__ = "event_list"

    el_id = db.Column(db.Integer, primary_key=True)
    _c_start_date = db.Column(db.Date)
    _c_end_date = db.Column(db.Date)
    el_group_id = db.Column(db.ForeignKey('group_list.gl_id'), nullable=False)
    el_student_id = db.Column(db.ForeignKey('student.s_id'), nullable=False)
    el_staff_id = db.Column(db.ForeignKey('staff_list.sl_id'), nullable=False)
    el_ec_id = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            "el_id": self.el_id,
            "el_c_start_date": self.el_c_start_date,
            "el_c_end_date": self.el_c_end_date,
            "el_group_id": self.el_group_id,
            "el_student_id": self.el_student_id,
            "el_staff_id": self.el_staff_id,
            "el_ec_id": self.el_ec_id
        }


    @property
    def el_c_start_date(self) -> str:
        return self._c_start_date.strftime("%Y-%m-%d")


    @el_c_start_date.setter
    def el_c_start_date(self, start_date: date) -> None:
        self._c_start_date = start_date


    @property
    def el_c_end_date(self) -> str:
        return self._c_end_date.strftime("%Y-%m-%d")


    @el_c_end_date.setter
    def el_c_end_date(self, end_date: date) -> None:
        self._c_end_date = end_date


    @classmethod
    def get_by_range(cls, date_from: date):
        if not date_from:
            raise ValueError('date_from is required')
        today = date.today()
        return cls.query.filter(
            cls.el_c_start_date.between(date_from, today) &
            cls.el_c_end_date.between(date_from, today)
        ).all()
