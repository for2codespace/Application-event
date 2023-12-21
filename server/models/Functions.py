from .db import db


class Function1(db.Model):
    __tablename__ = 'proc_event_list'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    c_start_date = db.Column(db.Date, nullable=False)
    c_end_date = db.Column(db.Date, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    staff_id = db.Column(db.Integer, nullable=False)