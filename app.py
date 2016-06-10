# coding: utf-8
from __future__ import unicode_literals

from flask import Flask, session, request
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
from flask_babelex import Babel

from config import Configuration
from db.base import db
from db.users import AdminUser
from db.admin_view import AdUserAdminView, StatisticView


app = Flask(__name__)
app.config.from_object(Configuration)

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# blueprint
from admin.admin import admin_bp
app.register_blueprint(admin_bp, url_prefix="/admin_bp")

# admin part
admin = Admin(app, name="空间站", template_mode="bootstrap3")
admin.add_view(AdUserAdminView(AdminUser, db.session, name="后台管理用户"))
admin.add_view(StatisticView(
    name='测试自定义', endpoint="statistic", category="测试"))
admin.add_view(StatisticView(
    name='测试自定义', endpoint="statistic2", category="测试"))


# i18n
babel = Babel(app)


@babel.localeselector
def get_locale():
    # 未来可使用这段代码提供语言选择
    # override = request.args.get('lang')
    # if override:
    #     session['lang'] = override
    # return session.get('lang', 'zh_CN')

    # 目前直接返回简体中文
    return "zh_CN"


if __name__ == '__main__':
    manager.run()
