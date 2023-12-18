from flask_restful import Resource
from models import StaffList as StaffListTable


class StaffList(Resource):
    path = "/staff_list"

    def get(self):
        staffs = StaffListTable.get_all()

        if staffs:
            return [s.json() for s in staffs]
        else:
            return {"message": "No staffs found"}, 404