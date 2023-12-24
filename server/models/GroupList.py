from .db import db


class GroupList(db.Model):
    __tablename__ = "group_list"

    gl_id = db.Column(db.Integer, primary_key=True)
    gl_name = db.Column(db.Integer, nullable=False)
    gl_year = db.Column(db.Date, nullable=False)

    def json(self):
        return {
            "gl_id": self.gl_id,
            "gl_name": self.gl_name,
            "gl_year": self.gl_year.__str__()
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
