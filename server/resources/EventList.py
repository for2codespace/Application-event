from flask_restful import Resource, request
from models import EventList as EventListTable


class EventList(Resource):
    path = "/event_list"

    @classmethod
    def get(cls):
        args = request.args

        if args.get('date_from'):
            date_from = map(int, args.get('date_from').split(' '))
        if args.get('date_to'):
            date_to = map(int, args.get('date_to').split(' '))

        events = EventListTable.get_by_range(date_from, date_to)

        if events:
            return {"events": [e.json() for e in events]}, 200
        else:
            return {"message": "No events found"}, 404
