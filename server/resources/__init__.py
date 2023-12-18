from flask_restful import Api
from .EventList import EventList
from .EventType import EventType
from .Groupes import Groupes
from .Report import Report
from .StaffList import StaffList
from .Student import Student
from .StudentBoard import StudentBoard


api = Api(prefix="/api")

for resource in [EventList, EventType, Groupes, Report, StaffList, Student, StudentBoard]:
    print(resource.path)
    api.add_resource(resource, resource.path)
