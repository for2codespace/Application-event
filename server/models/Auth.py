from .db import db, BaseModel
from passlib.hash import pbkdf2_sha256


class Auth(BaseModel):
    __tablename__ = "auth"

    staff_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(87), nullable=False)

    @classmethod
    def auth(cls, login, password):
        user = cls.query.filter_by(login=login).first()

        if not user:
            return False, -1

        if not pbkdf2_sha256.verify(password, user.password):
            return False, -1

        return True, user.staff_id
        