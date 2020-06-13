#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: gas_list.py
@time: 2020-03-30 23:09
"""
from base.element_manager import *


class GasList(BasePage):
    """油站列表页"""
    gas_name_nos_btn = 'new UiSelector().resourceId("com.xxx.xxx:id/oilName").text("更多加油站")'
    no_gas_card = (By.ID, 'com.xxx.xxx:id/ll_restart')
    gas_cards = (By.ID, 'com.xxx.xxx:id/gasStationName')
    gas_list_oil_no = (By.ID, 'com.xxx.xxx:id/gasOilNameView')
    gas_list_adv_close_btn = (By.ID, 'com.xxx.xxx:id/iv_close')
    gas_list_adv_face = (By.ID, 'com.xxx.xxx:id/bannerViewPager')

    @logged
    def check_in_gas_list(self):
        """是否进入油站列表页"""
        if self.is_element(*self.no_gas_card):
            logger.info("油站列表没显示油站～")
            return True
        else:
            return self.find_elements(*self.gas_name_nos_btn)

    @logged
    def click_gas_card_btn(self, index_no=0):
        """点击油站"""
        self.find_elements(*self.gas_cards)[index_no].click()

    @logged
    def get_oil_no_text(self):
        """获取油号"""
        text = self.find_element(*self.gas_list_oil_no).get_attribute('text')
        return text

    @logged
    def gas_list_adv(self, tap=False):
        """油站列表页广告处理"""
        if self.is_element(*self.gas_list_adv_face):
            if tap:
                self.find_element(*self.gas_list_adv_face).click()
            else:
                self.find_element(*self.gas_list_adv_close_btn).click()
