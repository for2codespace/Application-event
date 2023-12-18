from flask_restful import Resource
from models import EventType as EventTypeTable


class EventType(Resource):
    path = "/event_type"

    @classmethod
    def get(cls):
        events = EventTypeTable.get_all()

        if events:
            return {"event_types": [e.json() for e in events]}
        else:
            return {"message": "No events found"}, 404