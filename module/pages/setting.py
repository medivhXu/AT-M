#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: setting.py
@time: 2020-04-10 16:38
"""

from base.element_manager import *


class Setting(BasePage):
    """设置"""
    logout_btn = (By.ID, 'com.xxx.xxxx:id/loginOut')

    @logged
    def click_logout_btn(self):
        """点击登出"""
        self.find_element(*self.logout_btn).click()
