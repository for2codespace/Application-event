from flask_restful import Api
from .EventList import EventList
from .EventType import EventType
from .Groupes import Groupes
from .Report import Report
from .Staff import Staff
from .Student import Student
from .StudentBoard import StudentBoard


api = Api(prefix="/api")

for resource in [EventList, EventType, Groupes, Report, Staff, Student, StudentBoard]:
    api.add_resource(resource, resource.path)
