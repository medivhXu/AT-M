#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: first_page.py
@time: 2020-03-30 22:54
"""

from base.element_manager import *


class FirstPage(BasePage):
    """首页相关操作"""
    first_home_btn = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxx.xxxxxx:id/app_ty_home").text("首页")')
    gas_card_btn = (By.ID, 'com.xxx.xxxxxx:id/tv_start_oil')
    no_gas_card = (By.ID, 'com.xxx.xxxxxx:id/tv_no_sub_data_title')
    guide_layer = (By.XPATH,
                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View')
    order_info_btn = (By.ID, 'com.xxx.xxxxxx:id/app_ty_order')
    gun_name_btn = (By.ID, 'com.xxx.xxxxxx:id/gunName')
    quick_card_gas_name_btn = (By.ID, 'com.xxx.xxxxxx:id/tv_quick_oil_gas_name')
    quick_card_oil_no_btn = (By.ID, 'com.xxx.xxxxxx:id/tv_quick_sort_type')
    oil_no_list_btn = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.xxx.xxxxxx:id/ll_parent").{}')
    oil_no_list_title_text = (By.ID, 'com.xxx.xxxxxx:id/tv_title')
    more_gas_btn = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更多加油站")')

    @logged
    def click_immediately_add_oil(self, num=6):
        """点击快速加油"""
        if self.find_element(*self.no_gas_card):
            if num < 0:
                num -= 1
                logger.error("选了3个油号，但是首页一键加油还是没有油站～")
            self.click_oil_no(index=num)
            self.click_immediately_add_oil(num)
        else:
            self.find_element(*self.gas_card_btn).click()
        for i in range(num):
            if self.is_element(*self.gun_name_btn):
                self.find_element(*self.gun_name_btn).click()
                return self.find_element(*self.gun_name_btn).get_attribute('text')
            else:
                logger.info("网络异常或系统异常，找不到油站数据～")

    @logged
    def guide_cover_layer(self):
        """指南蒙层处理"""
        if self.is_in_first_page():
            if self.is_element(*self.guide_layer):
                self.find_element(*self.order_info_btn).click()
                self.find_element(*self.order_info_btn).click()
                self.find_element(*self.order_info_btn).click()
                self.find_element(*self.order_info_btn).click()
        else:
            logger.error("没进到主页，就要定位指南蒙层～")

    @logged
    def click_oil_no(self, oil_no='92', index: int = None):
        """
        点击油号

        只能单独用一个参数，同时使用优先用index
        :param oil_no:
        :param index:
        :return:
        """
        self.find_element(*self.quick_card_oil_no_btn).click()
        if self.find_element(*self.oil_no_list_title_text):
            if index:
                by, el = self.oil_no_list_btn
                el = el.format('index({})'.format(index))
                self.android_uiautomator(*(by, el)).click()
            else:
                oil_no = oil_no + '#'
                by, el = self.oil_no_list_btn
                el = el.format('text("{}")'.format(oil_no))
                self.android_uiautomator(*(by, el)).click()
        else:
            logger.warning("没弹出油号选择～")

    @logged
    def get_oil_no_text(self):
        """获取油号"""
        if self.is_element(*self.quick_card_oil_no_btn):
            gas_no_text = self.find_element(*self.quick_card_oil_no_btn).get_attribute('text')
            return gas_no_text

    @logged
    def click_more_gas_btn(self):
        """点击更多油站"""
        self.android_uiautomator(*self.more_gas_btn).click()

    @logged
    def is_in_first_page(self):
        """是否设置首页"""
        if self.find_element(*self.first_home_btn):
            self.find_element(*self.first_home_btn).get_attribute('checkable')
            return True
        else:
            return False

    @logged
    def click_first_page_btn(self):
        """点击首页"""
        self.android_uiautomator(*self.first_home_btn).click()
