# coding: utf-8
from passlib.apps import custom_app_context as pwd_context

from .base import db, AbstractBaseModel


class UserMixin(object):
    def hash_password(self, raw_password):
        self.encrypted_password = pwd_context.encrypt(raw_password)

    def verify_password(self, raw_password):
        return pwd_context.verify(raw_password, self.encrypted_password)


class AdminUser(AbstractBaseModel, UserMixin):
    __tablename__ = 'admin'
    username = db.Column(db.Unicode(20), nullable=False, unique=True)
    email = db.Column(db.Unicode(50), unique=True)
    encrypted_password = db.Column(db.Unicode(255), nullable=False)
