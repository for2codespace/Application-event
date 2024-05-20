from .db import db


class EventKind(db.Model):
    __tablename__ = "event_kind"
    ek_id = db.Column(db.Integer, primary_key=True)
    ek_name = db.Column(db.String(1000), nullable=False)

    def json(self):
        return {
            'ek_id': self.ek_id,
            'ek_name': self.ek_name
        }
