#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: __init__.py.py
@time: 2020-02-27 16:12
"""

from .account import *
from .order import *
from .pages import *
from .user import *


from base.android_keycode_enum import AndroidKeyCodeEnum


@logged
def other_login_flow(self):
    """
    其他手机号登录流程，模拟器和手机号都可以用
    :return
    """
    self.first_page.click_first_page_btn()
    self.first_page.click_immediately_add_oil()
    if self.login.in_login_page():
        self.login.click_login_btn()
    else:
        self.person_center.in_person_center()
        self.login.click_login_btn()
    self.login.click_other_phone_login_btn()
    self.phone, self.info = get_user_info_from_conf()
    self.login.input_phone_number(self.phone)
    self.login.click_send_msg_btn()
    self.login.input_code()
    self.login.click_next_btn()
    if self.login.is_msg_error_toast():
        self.login.input_code()
        self.login.click_next_btn()
        if self.login.is_msg_error_toast():
            logger.error("从新取完验证码还是错的！")
            return False
    self.first_page.guide_cover_layer()
    if self.order.is_in_order_list():
        self.order.press_keycode_by_android(AndroidKeyCodeEnum.BACK.value)
    return True


@logged
def reset_other_login_flow(self):
    """
    重置app之后 其他手机号登录流程，模拟器和手机号都可以用
    :return
    """
    self.login.always_allow_android(self.platform_version)
    self.advertising.close_user_agreement()
    self.advertising.update_now_app_window()
    self.login.always_allow_android(self.platform_version)
    if self.login.in_login_page():
        self.login.click_login_btn()
    else:
        self.person_center.in_person_center()
        self.login.click_login_btn()
    self.login.click_other_phone_login_btn()
    self.login.input_phone_number(self.phone)
    self.login.click_send_msg_btn()
    self.login.input_code()
    self.login.click_next_btn()
    if self.login.is_msg_error_toast():
        self.login.input_code()
        self.login.click_next_btn()
        if self.login.is_msg_error_toast():
            logger.error("从新取完验证码还是错的！")
            return False
    self.first_page.guide_cover_layer()
    if self.order.is_in_order_list():
        self.order.press_keycode_by_android(AndroidKeyCodeEnum.BACK.value)
    return True


@logged
def local_phone_login_flow(self):
    """
    本地一键登录，进入个人中心校验用户信息
    注：只能用有sim卡的手机进行测试
    """
    self.first_page.click_first_page_btn()
    self.first_page.click_immediately_add_oil()
    self.login.click_login_btn()
    phone_text = self.login.get_phone_login_number_text()
    self.login.local_phone_login_btn()
    self.first_page.guide_cover_layer()
    self.person_center.in_person_center()
    center_phone = self.person_center.get_user_phone_text()
    if phone_text == center_phone:
        self.first_page.click_first_page_btn()
        return True
    else:
        return False


@logged
def reset_local_phone_login_flow(self):
    """重置app之后 本地手机号登录流程"""
    self.login.always_allow_android(self.platform_version)
    self.advertising.close_user_agreement()
    self.advertising.update_now_app_window()
    self.login.always_allow_android(self.platform_version)
    self.login.click_login_btn()
    phone_text = self.login.get_phone_login_number_text()
    self.login.local_phone_login_btn()
    self.first_page.guide_cover_layer()
    self.person_center.in_person_center()
    if self.person_center.is_ad_window():
        self.person_center.click_ad_window_close_btn()
    center_phone = self.person_center.get_user_phone_text()
    if phone_text == center_phone:
        self.first_page.click_first_page_btn()
        return True
    else:
        return False


@logged
def set_pwd_flow(self):
    """
    设置交易密码流程
    :return
    """
    env = conf_load('../__conf.yaml').read().get('MYSQL')
    delete_pwd_by_phone(env=env, phone=self.phone)
    self.check_stand.click_set_password_dialog()
    self.set_pay_pwd.click_send_msg_btn()
    code = get_msg_from_db(self.phone)
    self.set_pay_pwd.input_msg_code_in_box(code=code)
    self.set_pay_pwd.input_pay_password_in_box()
    self.set_pay_pwd.input_pay_password_again_in_box()
    self.set_pay_pwd.click_right_btn()
    self.check_stand.click_pay_finish_btn()
    return True
