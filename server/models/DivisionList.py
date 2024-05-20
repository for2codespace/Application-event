from .db import db


class DivisionList(db.Model):
    __tablename__ = "division_list"

    dl_id = db.Column(db.Integer, primary_key=True)
    dl_name = db.Column(db.String(50), nullable=False)
    dl_parent_division_id = db.Column(db.Integer, nullable=True)

    def json(self):
        return {
            "dl_id": self.dl_id,
            "dl_name": self.dl_name,
            "dl_parent_division_id": self.dl_parent_division_id
        }