from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError


db = SQLAlchemy()

db.ConnectionError = OperationalError


class GetableNone:
    def __getattr__(self, item):
        return GetableNone()

    def __str__(self):
        return "null"


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        result = cls.query.get(id) 
        if not result:
            return GetableNone()
        else:
            return result

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()