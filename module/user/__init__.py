#!/usr/bin/env python3
"""
@author: Medivh Xu
@file: __init__.py.py
@time: 2020-04-10 14:12
"""

from .get_msg_from_db import *
from .user import *
from base.logged import *
from config_loader import conf_load


@logged
def create_user_of_level_3_funrun(phone, user_info, **env):
    """
    自动创建三级分润用户
    :param phone:
    :param user_info:
    :param env:
    :return:
    """
    new_user = User(user_info, **env)
    if not new_user.get_user_info_by_phone(phone):
        new_user_id = new_user.add_user_info(phone)
        user_info['user_id'] = new_user_id
        new_user.set_auth_by_user_id(user_info)
    else:
        new_user.update_user_info(phone)
    new_user.set_level_3_funrun(phone)


@logged
def delete_user(phone, **env):
    old_user = User(**env)
    user_info = old_user.get_user_info_by_phone(phone)
    if not len(user_info):
        return True
    else:
        r = old_user.delete_user_info_by_phone(phone)
        r_auth = old_user.delete_auth_by_user_id(user_id=user_info[0].get('user_id'))
        if r and r_auth:
            return True
        else:
            return False


@logged
def get_user_id_by_phone(phone, **env):
    old_user = User(**env)
    user_info = old_user.get_user_info_by_phone(phone)
    try:
        user_id = user_info[0].get('user_id')
        return user_id
    except IndexError:
        raise RuntimeException("没找到用户！")


@logged
def get_user_info_by_phone(phone, **env):
    old_user = User(env)
    user_info = old_user.get_user_info_by_phone(phone)
    return user_info


@logged
def get_user_auth_by_user_id(user_id, **env):
    old_user = User(env)
    user_auth = old_user.get_auth_by_user_id(user_id)
    return user_auth


@logged
def get_user_info_from_conf():
    user_conf = conf_load('user.yaml').read()
    for k, v in user_conf.items():
        return k, v


@logged
def delete_pwd_by_phone(phone, **env):
    """
    删除用户支付密码
    :return
    """
    old_user = User(**env)
    old_user.delete_user_pwd_by_phone(phone)
    return True
