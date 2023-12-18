from flask_restful import Resource
from models import Student as StudentTable


class Student(Resource):
    path = "/student"

    @classmethod
    def get(cls):
        students = StudentTable.get_all()

        if students:
            return {"students": [s.json() for s in students]}
        else:
            return {"message": "No students found"}, 404