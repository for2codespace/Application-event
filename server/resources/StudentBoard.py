from flask_restful import Resource
from models import StudentBoard as StudentBoardTable


class StudentBoard(Resource):
    path="/student_board"
    
    def get(self):
        students = StudentBoardTable.get_all()

        if students:
            return {"board": [s.json() for s in students]}, 200
        else:
            return {"message": "No students boards found"}, 404