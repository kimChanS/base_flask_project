# coding: utf-8

from flask import Blueprint

from db.users import AdminUser

admin_bp = Blueprint('admin_pages', __name__)


@admin_bp.route("/")
def index():
    return "hello world"
