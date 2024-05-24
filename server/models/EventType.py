from .db import db, BaseModel


class EventType(BaseModel):
    __tablename__ = "event_type"

    et_id = db.Column(db.Integer, primary_key=True)
    et_name = db.Column(db.String(200), nullable=False)
    et_location = db.Column(db.String(50))
    et_calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.c_id'), nullable=False)
    et_ek_id = db.Column(db.Integer, db.ForeignKey('event_kind.ek_id'), nullable=False)

    def json(self):
        return {
            "et_id": self.et_id,
            "et_name": self.et_name,
            "et_location": self.et_location,
            "et_calendar_id": self.et_calendar_id,
            "et_ek_id": self.et_ek_id
        }
