# coding: utf-8
import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# bind db and specify idx/fk...'s name rule
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)


class AbstractBaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime(), default=datetime.datetime.now())
    update_time = db.Column(
        db.DateTime(),
        default=datetime.datetime.now(), onupdate=datetime.datetime.now())
