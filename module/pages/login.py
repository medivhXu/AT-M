#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: test_login.py
@time: 2020-03-20 14:10
"""

from module.user import *
from base.element_manager import *

from base.android_keycode_enum import AndroidKeyCodeEnum


class Login(BasePage):
    """登录"""
    desensitization_phone_text = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(".*\\*.*")')
    login_btn = (By.ID, 'com.xxx.xxx:id/phoneLogin')
    local_phone_btn = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("本机号码一键登录")')
    other_phone_btn = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("其他手机号码登录")')
    phone_box = (By.ID, 'com.xxx.xxx:id/phoneNumberView')
    send_msg_btn = (By.ID, 'com.xxx.xxx:id/sendMsgBtn')
    msg_box = (By.ID, 'com.xxx.xxx:id/codeNumberView')
    next_btn = (By.ID, 'com.xxx.xxx:id/nextBtn')

    @logged
    def in_login_page(self):
        """是否进入登录页面"""
        if self.find_element(*self.login_btn):
            return True
        else:
            logger.warning("没进入登录页面～")
            return False

    @logged
    def click_login_btn(self):
        """点击登录按钮"""
        self.find_element(*self.login_btn).click()

    @logged
    def local_phone_login_btn(self, num=3):
        """本地手机号登录"""
        while True:
            if self.android_uiautomator(*self.local_phone_btn):
                self.android_uiautomator(*self.local_phone_btn).click()
                break
            else:
                if self.android_uiautomator(*self.other_phone_btn):
                    logger.info("手机号登录页面居然没出现本地手机号登录按钮～")
                    self.press_keycode_by_android(AndroidKeyCodeEnum.BACK.value)
                    self.click_login_btn()
                else:
                    logger.info("不知道跑哪页去了～")
            num -= 1
            if num == 0:
                logger.error("重新进了n次都没有本地一键登录按钮，是不是忽悠我～")
                break

    @logged
    def get_phone_login_number_text(self):
        """获取登录手机号"""
        desensitization_phone = self.android_uiautomator(*self.desensitization_phone_text).get_attribute('text')
        return desensitization_phone

    @logged
    def click_other_phone_login_btn(self):
        """点击其他手机号登录"""
        if self.android_uiautomator(*self.other_phone_btn):
            self.android_uiautomator(*self.other_phone_btn).click()
        else:
            logger.warning("没弹本地手机号和其他手机号选择页！")
            pass

    @logged
    def input_phone_number(self, phone):
        """输入手机号"""
        self.find_element(*self.phone_box).send_keys(phone)

    @logged
    def click_send_msg_btn(self):
        """点击发送短信"""
        self.find_element(*self.send_msg_btn).click()

    @logged
    def input_code(self):
        """输入验证码"""
        if self.is_element(*self.msg_box):
            self.find_element(*self.msg_box).clear()
            phone, info = get_user_info_from_conf()
            code = get_msg_from_db(phone)
            self.find_element(*self.msg_box).send_keys(code)
        else:
            self.click_send_msg_btn()

    @logged
    def is_msg_error_toast(self):
        """是否toast提示验证码错误"""
        return self.is_toast_exist('验证码错误')

    @logged
    def click_next_btn(self):
        """点击下一步"""
        self.find_element(*self.next_btn).click()
