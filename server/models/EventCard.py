from .db import db, BaseModel
from .EventList import EventList
from .EventKind import EventKind
from .EducationalActivitiesType import EducationalActivitiesType


class EventCard(BaseModel):
    __tablename__ = "event_card"

    ec_id = db.Column(db.Integer, primary_key=True)
    ec_name = db.Column(db.String(1000), nullable=False)
    ec_is_planned_work = db.Column(db.Boolean, nullable=False)
    ec_location = db.Column(db.String(1000), nullable=False)
    ec_is_photo_exists = db.Column(db.Boolean, nullable=False)
    ec_internal_link = db.Column(db.String(1000))
    ec_external_link = db.Column(db.String(1000))
    ec_eat_id = db.Column(db.Integer, db.ForeignKey('educational_activities_type.eat_id'))
    ec_ek_id = db.Column(db.Integer, db.ForeignKey('event_kind.ek_id'))
    ec_comments = db.Column(db.String(1000))


    def json(self):
        event_act_type = EducationalActivitiesType.get_by_id(self.ec_eat_id)
        event_kind = EventKind.get_by_id(self.ec_ek_id)
        event_list = EventList.get_by_ec_id(self.ec_id)
        return {
            'ec_id': self.ec_id,
            'ec_name': self.ec_name,
            'ec_is_planned_work': self.ec_is_planned_work,
            'ec_location': self.ec_location,
            'ec_is_photo_exists': self.ec_is_photo_exists,
            'ec_internal_link': self.ec_internal_link,
            'ec_external_link': self.ec_external_link,
            'ec_comments': self.ec_comments,
            # foreign fields
            'ec_eat_id':  event_act_type.json() if event_act_type else None,
            'ec_ek_id':   event_kind.json()     if event_kind else None,
            'event_list': event_list.json()     if event_list else None
        }