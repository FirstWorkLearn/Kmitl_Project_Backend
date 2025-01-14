from app import db
from datetime import datetime

class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    des = db.Column(db.String(255))
    price = db.Column(db.String(255))
    tag = db.Column(db.String(255))
    warning = db.Column(db.String(255))

    def __init__(self, type_id, name, image, des=None, price=None, tag=None, warning=None):
        self.type_id = type_id
        self.name = name
        self.image = image
        self.des = des
        self.price = price
        self.tag = tag
        self.warning = warning

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
