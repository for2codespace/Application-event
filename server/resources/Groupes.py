from flask_restful import Resource
from models import GroupList as GroupListTable


class Groupes(Resource):
    path = "/groupes"

    @classmethod
    def get(cls):
        groupes = GroupListTable.get_all()

        if groupes:
            return {"groupes": [g.json() for g in groupes]}, 200
        else:
            return {"message": "No groupes found"}, 404