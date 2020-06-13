#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: order_finished.py
@time: 2020-03-30 23:14
"""

from base.element_manager import *


class OrderFinished(BasePage):
    """订单完成页"""
    order_finished_ad_close_btn = (By.ID, 'com.xxx.xxx:id/iv_close')
    order_id_number = (By.ID, 'com.xxx.xxx:id/data_odd_number')
    advertising_window = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ImageView')
    order_finished_success = (By.ID, 'com.xxx.xxx:id/tv_pay_suc')
    order_refund_btn = (By.ID, 'com.xxx.xxx:id/tv_refund_btn')

    @logged
    def is_ad_window(self):
        """是否弹出广告"""
        return self.find_element(*self.order_finished_ad_close_btn)

    @logged
    def click_ad_close_btn(self):
        """点击关闭广告"""
        self.find_element(*self.order_finished_ad_close_btn).click()

    @logged
    def click_ad_window(self):
        """点击广告弹窗"""
        self.find_element(*self.advertising_window).click()
        return self

    @logged
    def get_order_finished_status_text(self):
        """获取订单状态"""
        text = self.find_element(*self.order_finished_success).get_attribute('text')
        return text

    @logged
    def get_refund_btn_text(self):
        """获取申请退单"""
        text = self.find_element(*self.order_refund_btn).get_attribute('text')
        return text

    @logged
    def get_order_number_text(self):
        """获取订单号"""
        text = self.find_element(*self.order_id_number).get_attribute('text')
        return text
