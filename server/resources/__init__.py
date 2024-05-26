from flask_restful import Api
from .EventType import EventType
from .Groups import Groups
# from .Report import Report
from .Staff import Staff
from .Student import Student
from .StudentBoard import StudentBoard
from .EventCard import EventCard
from .DOCS import Docs
from .Auth import Auth, Logout
from .EatList import EatList
from .EventKindList import EventKindList


api = Api(prefix="/api")

for resource in [
    Logout,
    EventKindList,
    EatList,
    EventCard,
    EventType,
    Groups,
    # Report,
    Auth,
    Staff,
    Student,
    StudentBoard,
    Docs
]:
    print("binding:", resource.path)
    api.add_resource(resource, resource.path)
