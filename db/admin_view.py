# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_admin.model import typefmt
from wtforms.fields import PasswordField
from wtforms.validators import DataRequired


# 自定义前端显示格式
def date_format(view, value):
    return value.strftime('%Y/%m/%d %H:%M:%S')

MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({
    # type(None): typefmt.null_formatter,
    datetime: date_format
})


class BaseModelView(ModelView):
    # 可排序的列
    column_sortable_list = ['create_time', 'update_time']
    # 不显示的列
    column_exclude_list = ['encrypted_password']
    column_type_formatters = MY_DEFAULT_FORMATTERS

    # 新增/修改时, 不需要的列
    form_excluded_columns = ['create_time', 'update_time']
    # 重定义密码的类型为password
    form_extra_fields = {
        "encrypted_password": PasswordField(
            '密码', validators=[DataRequired()])
    }


class AdUserAdminView(BaseModelView):
    """
    管理admin user
    """
    can_delete = False
    # create_modal = True
    # edit_modal = True
    # can_export = True
    column_list = ('username', 'email', 'create_time', 'update_time')
    column_searchable_list = ('username', 'email')
    column_default_sort = ('update_time', True)
    column_labels = dict(
        username='用户名',
        email="邮箱",
        create_time="创建时间",
        update_time="修改时间"
    )

    def on_model_change(self, form, model, is_created):
        # 加密密码
        if len(model.encrypted_password):
            model.hash_password(model.encrypted_password)


class StatisticView(BaseView):
    @expose("/")
    def index(self):
        return "hello statistic"
