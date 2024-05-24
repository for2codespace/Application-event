from flask_restful import Resource
from models import Student as StudentTable
from .Auth import auth_required


class Student(Resource):
    path = "/student"

    @classmethod
    @auth_required
    def get(cls, id):
        students = StudentTable.all()

        if students:
            return {"students": [s.json() for s in students]}
        else:
            return {"message": "No students found"}, 404