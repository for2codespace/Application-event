from flask_restful import Resource
from models import EventList as EventListTable


class Report(Resource):
    path = "/report"

    @classmethod
    def get(cls):
        events = EventListTable.get_all()

        if events:
            return [e.json() for e in events]
        else:
            return {"message": "No events found"}, 404