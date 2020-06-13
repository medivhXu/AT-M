#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: order.py
@time: 2020-03-31 14:40
"""

from base.element_manager import *


class Order(BasePage):
    """订单"""
    order_list_title = (By.ID, 'com.xxx.xxx:id/tv_title')

    @logged
    def is_in_order_list(self):
        """是否进入订单列表页"""
        return self.find_element(*self.order_list_title)
