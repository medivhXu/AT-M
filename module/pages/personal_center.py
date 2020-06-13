#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: personal_center.py
@time: 2020-03-30 16:24
"""
from base.element_manager import *


class PersonCenter(BasePage):
    """个人中心"""
    person_center_btn = (By.ID, 'com.xxx.xxx:id/app_ty_mine')
    phone_text = (By.ID, 'com.xxx.xxx:id/tv_user_phone')
    authen_type = (By.ID, 'com.xxx.xxx:id/tv_auth_car')
    vip_status = (By.ID, 'com.xxx.xxx:id/tv_vip_type')
    setting_btn = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设置")')
    person_center_ad_window = (By.ID, 'com.xxx.xxx:id/bannerViewPager')
    person_center_ad_window_close_btn = (By.ID, 'com.xxx.xxx:id/iv_close')

    @logged
    def in_person_center(self):
        """是否进入个人中心"""
        self.find_element(*self.person_center_btn).click()

    @logged
    def get_user_phone_text(self):
        """获取用户手机号"""
        while True:
            # 如果手机号元素没出来就一直点个人中心
            if self.is_element(*self.phone_text):
                phone = self.find_element(*self.phone_text).get_attribute('text')
                return phone
            else:
                self.in_person_center()

    @logged
    def is_ad_window(self):
        """是否弹出广告"""
        return self.find_element(*self.person_center_ad_window)

    @logged
    def click_ad_window_close_btn(self):
        """点击广告关闭按钮"""
        self.find_element(*self.person_center_ad_window_close_btn).click()

    @logged
    def get_authen_type_text(self):
        """获取用户认证类型"""
        authen_text = self.find_element(*self.authen_type).get_attribute("text")
        return authen_text

    @logged
    def get_vip_text(self):
        """获取用户会员级别"""
        vip_text = self.find_element(self.vip_status).get_attribute('text')
        return vip_text

    @logged
    def click_setting_btn(self):
        """点击设置按钮"""
        self.android_uiautomator(*self.setting_btn).click()
