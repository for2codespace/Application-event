from flask_restful import Resource, request as req
from models import EventList as EventListTable
import datetime as date


def parse_string_date(string_date: str) -> date:
    # 2020-01-01 => ['2020', '01', '01']
    date_array = string_date.split('-')
    year = int(date_array[0])   # ['2020', '01', '01'] => 2020, 01, 01
    month = int(date_array[1])
    day = int(date_array[2])
    return date(year, month, day)


class EventList(Resource):
    path = "/event_list"

    @classmethod
    def get(cls):
        try:
            string_date = req.args['date']
            if not string_date:
                raise ValueError
            date = parse_string_date(string_date)
            events = EventListTable.get_by_range(date)
        except Exception as e:
            events = EventListTable.get_all()

        if events:
            return {"events": [e.json() for e in events]}, 200
        else:
            return {"message": "No events found"}, 404

    @classmethod
    def post(cls):
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
