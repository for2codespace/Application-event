from flask_restful import request, Resource

from models import EventCard as EventCardTable
from .Auth import auth_required


class EventCard(Resource):
    path = "/event_cards"

    
    @classmethod
    @auth_required
    def get(cls, id):
        ec_id = request.args.get('id')
        print(ec_id)
        if ec_id:
            event_card = EventCardTable.get_by_id(ec_id)
            return {"event_card": event_card.json()}
        else:
            event_cards = EventCardTable.all()
            return {"event_cards": [event_card.json() for event_card in event_cards]}