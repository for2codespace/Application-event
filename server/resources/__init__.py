from flask_restful import Api
from .EventList import EventList
from .EventType import EventType
from .Groups import Groups
from .Report import Report
from .Staff import Staff
from .Student import Student
from .StudentBoard import StudentBoard
from .DOCS import Docs


api = Api(prefix="/api")

for resource in [EventList, EventType, Groups, Report, Staff, Student, StudentBoard, Docs]:
    api.add_resource(resource, resource.path)
