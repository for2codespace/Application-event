from .db import db


class GroupList(db.Model):
    __tablename__ = "GROUP_LIST"

    GL_ID = db.Column(db.Integer, primary_key=True)
    GL_NAME = db.Column(db.Integer, nullable=False)
    GL_NUMBER = db.Column(db.Integer, nullable=False)
    GL_YEAR = db.Column(db.Date, nullable=False)

    def json(self):
        return {
            "GL_ID": self.GL_ID,
            "GL_NAME": self.GL_NAME,
            "GL_NUMBER": self.GL_NUMBER,
            "GL_YEAR": self.GL_YEAR.__str__()
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
