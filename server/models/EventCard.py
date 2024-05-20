from .db import db


class EventCard(db.Model):
    __tablename__ = "event_card"

    ec_id = db.Column(db.Integer, primary_key=True)
    ec_name = db.Column(db.String(1000), nullable=False)
    ec_is_planned_work = db.Column(db.Boolean, nullable=False)
    ec_location = db.Column(db.String(1000), nullable=False)
    ec_is_photo_exists = db.Column(db.Boolean, nullable=False)
    ec_internal_link = db.Column(db.String(1000))
    ec_external_link = db.Column(db.String(1000))
    ec_eat_id = db.Column(db.ForeignKey('event_activities_type.eat_id'))
    ec_ek_id = db.Column(db.ForeignKey('event_kind.ek_id'))
    ec_comments = db.Column(db.String(1000))


    def json(self):
        return {
            'ec_id': self.ec_id,
            'ec_name': self.ec_name,
            'ec_is_planned_work': self.ec_is_planned_work,
            'ec_location': self.ec_location,
            'ec_is_photo_exists': self.ec_is_photo_exists,
            'ec_internal_link': self.ec_internal_link,
            'ec_external_link': self.ec_external_link,
            'ec_eat_id': self.ec_eat_id,
            'ec_ek_id': self.ec_ek_id,
            'ec_comments': self.ec_comments
        }