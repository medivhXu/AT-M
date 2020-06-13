#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: advertising.py
@time: 2020-03-30 16:40
"""
from base.element_manager import *


class Advertising(BasePage):
    """首页广告类相关操作"""
    user_agreement_title = (By.ID, 'com.xxx.xxx:id/handleLayout')
    user_agreement_btn = (By.ID, 'com.xxx.xxxxx:id/tv_center')
    update_now = (By.ID, 'com.xxx.xxxxx:id/upGrade')
    update_later = (By.ID, 'com.xxx.xxxxx:id/close')

    @logged
    def close_user_agreement(self):
        """关闭用户协议"""
        if self.find_element(*self.user_agreement_btn):
            self.find_element(*self.user_agreement_btn).click()
        else:
            logger.info("没弹出用户协议～")

    @logged
    def update_now_app_window(self, switch=True):
        """非强更弹窗处理"""
        if self.find_element(*self.update_now):
            if switch:
                self.find_element(*self.update_later).click()
            else:
                self.find_element(*self.update_now).click()


