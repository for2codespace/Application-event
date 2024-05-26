from datetime import date

from flask_restful import request, Resource

from models import EventCard as EventCardTable
from .Auth import auth_required


class EventCard(Resource):
    path = "/event_cards"
    
    @classmethod
    @auth_required
    def get(cls, id):
        ec_id = request.args.get('id')
        date_start, date_end = request.args.get('date_start'), request.args.get('date_end')
        if ec_id:
            event_card = EventCardTable.get_by_id(ec_id)
            return {"event_card": event_card.json()}
        else:
            if all([date_start, date_end]):
                date_start = str2date(date_start)
                date_end = str2date(date_end)
                event_cards = EventCardTable.get_by_range(date_start, date_end)
                return {"event_cards": [event_card.json() for event_card in event_cards]}
            else:
                event_cards = EventCardTable.all()
                return {"event_cards": [event_card.json() for event_card in event_cards]}

    @classmethod
    @auth_required
    def post(cls):
        name = request.args.get('name')
        is_planned_work = request.args.get('is_planned_work')
        ec_location = request.args.get('location')
        ec_is_photo_exists = request.args.get('is_photo_exists')
        ec_eat_id = request.args.get('eat_id')
        ec_ek_id = request.args.get('ek_id')
        # event_visit_student_group
        ec_staff_id = request.args.get('staff_id')



def str2date(date_str):
    yy, mm, dd = map(int, date_str.split('-'))
    return date(yy, mm, dd)