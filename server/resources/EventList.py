from flask_restful import Resource, request
from models import EventList as EventListTable
from datetime import date


class EventList(Resource):
    path = "/event_list"

    @classmethod
    def get(cls):
        args = request.args  # ?key1=value1 -> {key1: value}

        if args and args.get('date_from') and args.get('date_to'):
            try:
                print(
                    *map(int, args.get('date_from').split('-')), 
                    ";",
                    *map(int, args.get('date_to').split('-'))
                )
                events = EventListTable.get_by_range(
                    date(*map(int, args.get('date_from').split('-'))), # "2023-12-21" -> [2023, 12, 21]
                    date(*map(int, args.get('date_to').split('-'))),   # date(year, month, day)
                )
            except ValueError or AttributeError as e:
                print("Exception: {}".format(e))
                events = EventListTable.get_all()
        else:
            print("else")
            events = EventListTable.get_all()

        if events:
            return {"events": [e.json() for e in events]}, 200
        else:
            return {"message": "No events found"}, 404
