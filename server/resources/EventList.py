from flask_restful import Resource, request as req
from models import EventList as EventListTable
from datetime import date
from .Auth import auth_required


def str2date(string_date: str) -> date:
    date_array = string_date.split('-')
    year, month, day = map(int, date_array)
    return date(year, month, day)


class EventList(Resource):
    path = "/event_list"

    @classmethod
    @auth_required
    def get(cls, id):
        try:
            date_from = req.args.get('date_from')
            date_to = req.args.get('date_to')

            if not date_from and not date_to:
                return {"events": [e.json() for e in EventListTable.all()]}, 200
            
            events = EventListTable.get_by_range(
                str2date(date_from),
                str2date(date_to)
            )
        except Exception as e:
            return {"message": "Invalid date format", "error": str(e)}, 400

        if events:
            return {"events": [e.json() for e in events]}, 200
        else:
            return {"message": "No events found"}, 404

    @classmethod
    @auth_required
    def post(cls, id):
        json_body = req.json
        REQUIRED_ARGS = [
            "calendar_id", "event_type_id", "c_start_date", "c_end_date", "group_id", "student_id", "staff_id"
        ]
        for arg in REQUIRED_ARGS:
            if arg not in json_body:
                return {"message": f"Missing argument: {arg}"}, 400
        
        prefix = "el_"
        filtered_json_body = { prefix+key: json_body[key] for key in REQUIRED_ARGS }
        event = EventListTable(**filtered_json_body)
        event.save()

        return {"message": "Event created"}, 201
