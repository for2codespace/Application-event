from flask_restful import Resource
from models import GroupList as GroupListTable


class Groups(Resource):
    path = "/groups"

    @classmethod
    def get(cls):
        groupes = GroupListTable.get_all()

        if groupes:
            return {"groups": [g.json() for g in groupes]}, 200
        else:
            return {"message": "No groups found"}, 404
