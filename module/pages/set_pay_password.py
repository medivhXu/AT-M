#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: set_pay_password.py
@time: 2020-04-09 15:22
"""

import time

from base.element_manager import *


class SetPayPassword(BasePage):
    """设置支付密码"""
    phone_number = (By.ID, 'com.xxx.xxx:id/phoneNumber')
    msg_btn = (By.ID, 'com.xxx.xxx:id/getMessage')
    msg_input_box = (By.ID, 'com.xxx.xxx:id/inputMessage')
    password_input_box = (By.ID, 'com.xxx.xxx:id/passWord')
    password_input_again_box = (By.ID, 'com.xxx.xxx:id/passWord2')
    right_btn = (By.ID, 'com.xxx.xxx:id/confirm_btn')

    @logged
    def get_phone_number_text(self) -> str:
        """获取手机号"""
        text = self.find_element(*self.phone_number).get_attribute('text')
        return text

    @logged
    def click_send_msg_btn(self, num=3):
        """点击发送验证码"""
        while True:
            self.find_element(*self.msg_btn).click()
            time.sleep(0.5)
            if '重新发送' in self.find_element(*self.msg_btn).get_attribute('text'):
                break
            else:
                num -= 1
                if num == 0:
                    logger.error("设置交易密码失败～可能是网络原因")
                    break

    @logged
    def input_msg_code_in_box(self, code):
        """输入验证码"""
        self.find_element(*self.msg_input_box).send_keys(code)

    @logged
    def input_pay_password_in_box(self, password=333333):
        """输入支付密码"""
        self.find_element(*self.password_input_box).send_keys(password)

    @logged
    def input_pay_password_again_in_box(self, password=333333):
        """再次输入支付密码"""
        self.find_element(*self.password_input_again_box).send_keys(password)

    @logged
    def click_right_btn(self):
        """点击确定"""
        self.find_element(*self.right_btn).click()
