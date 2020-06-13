#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: gas.py
@time: 2020-03-30 15:29
"""

from base.element_manager import *


class GasInfo(BasePage):
    """油站详情"""
    gun_name_btn = (By.ID, 'com.xxx.xxx:id/gunName')
    money_input_box = (By.ID, 'com.xxx.xxx:id/et_input_money')
    money_btn = (By.ID, 'com.xxx.xxx:id/tv_money_{}')
    next_btn = (By.ID, 'com.xxx.xxx:id/bt_confirm')
    continue_card = (By.ID, 'android:id/content')
    continue_next_btn = (By.ID, 'com.xxx.xxx:id/tv_pay')
    reset_next_btn = (By.ID, 'com.xxx.xxx:id/reset_btn')
    oil_no_btn = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxx.xxx:id/oilName").text("{}")')
    price = (By.ID, 'com.xxx.xxx:id/xxxPrice')

    @logged
    def click_gun_no(self):
        """点击油枪"""
        self.find_element(*self.gun_name_btn).click()

    @logged
    def get_gun_no_text(self):
        """获取枪号"""
        return self.find_element(*self.gun_name_btn).get_attribute('text')

    @logged
    def click_oil_no_text(self, oil_no):
        """点击油号"""
        by, el = self.oil_no_btn
        return self.android_uiautomator(*(by, el.format(oil_no))).click()

    @logged
    def click_money_btn(self, btn_num=1):
        """点击金额"""
        by, el = self.money_btn
        el = el.format(btn_num)
        self.hide_keyboard()
        if self.find_element(*(by, el)).get_attribute('clickable'):
            # 定位到金额1按钮
            self.find_element(*(by, el)).click()
        else:
            logger.info("弹出系统键盘了")
            # self.hide_keyboard()
            self.find_element(*(by, el)).click()

    @logged
    def get_input_money_text(self):
        """获取输入金额"""
        text = self.find_element(*self.money_input_box).get_attribute('text')
        return text

    @logged
    def click_next_btn(self):
        """点击下一步"""
        self.hide_keyboard()
        self.find_element(*self.next_btn).click()

    @logged
    def click_continue_next_btn(self, switch=True):
        """点击继续支付"""
        if self.find_element(*self.continue_card):
            if switch:
                self.find_element(*self.continue_next_btn).click()
            else:
                self.find_element(*self.reset_next_btn).click()
        else:
            self.click_next_btn()

    @logged
    def input_money(self, money):
        """输入金额"""
        self.find_element(*self.money_input_box).clear()
        self.find_element(*self.money_input_box).send_keys(money)

    @logged
    def check_oil_no(self, check_oil_no_text):
        """ TODO 目前这个方法有问题，需要图像识别重写
        检车油号是否选择
        """
        by, el = self.oil_no_btn
        el = el.format(check_oil_no_text)
        text = self.android_uiautomator(*(by, el))
        return text

    @logged
    def get_price_text(self):
        """获取当前油号价格"""
        price = self.find_element(*self.price).get_attribute('text')
        return price
