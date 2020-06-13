#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: order.py
@time: 2020-03-30 15:29
"""
from base.element_manager import *


class CheckStand(BasePage):
    """收银台相关操作"""
    pay_finish_btn = (By.ID, 'com.xxx.xxxxxx:id/tv_pay_confirm')
    password_keyboard = (By.ID, 'com.xxx.xxxxxx:id/keyView')
    oil_no_text = (By.ID, '	com.xxx.xxxxxx:id/tv_oil_order_oil_num')
    gun_no_text = (By.ID, 'com.xxx.xxxxxx:id/tv_oil_order_guns')
    input_money_text = (By.ID, 'com.xxx.xxxxxx:id/tv_oil_order_price')
    straight_down = (By.ID, 'com.xxx.xxxxxx:id/tv_oil_offers_price')
    coupon_selected = (By.ID, 'com.xxx.xxxxxx:id/tv_oil_offers_coupon')
    coupon_card = (By.ID, 'com.xxx.xxxxxx:id/rl_coupon_bg')
    total_balance = (By.ID, 'com.xxx.xxxxxx:id/tv_available_blance')
    available_balance = (By.ID, 'com.xxx.xxxxxx:id/tv_available_balance_pay')
    balance_pay_btn = (By.ID, 'com.xxx.xxxxxx:id/v_available_user_balance')
    other_pay_btn = (By.ID, 'com.xxx.xxxxxx:id/view_check')
    no_use_coupon = (By.ID, 'com.xxx.xxxxxx:id/rl_no_use')
    puls_vip_btn = (By.ID, 'com.xxx.xxxxxx:id/cb_plus_vip_pay')
    red_package_default = (By.ID, 'com.xxx.xxxxxx:id/tv_red_paper_price')
    red_package = (By.XPATH,
                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[{}]')
    total_money = (By.ID, 'com.xxx.xxxxxx:id/tv_wait_payment_price_noVip')
    wechat_pay_money = (By.XPATH,
                        '//android.widget.FrameLayout[@content-desc="当前所在页面,支付"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView')
    set_password_dialog_message = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout')
    password_dialog_right = (By.ID, 'com.xxx.xxxxxx:id/tv_right')
    password_dialog_cancel = (By.ID, 'com.xxx.xxxxxx:id/tv_left')
    forget_pwd = (By.ID, 'com.xxx.xxxxxx:id/tv_forget_pwd')
    cancel_dialog = (By.ID, 'com.xxx.xxxxxx:id/tv_title')
    cancel_dialog_quit_btn = (By.ID, 'com.xxx.xxxxxx:id/tv_left')
    cancel_dialog_continue = (By.ID, 'com.xxx.xxxxxx:id/tv_right')

    @logged
    def click_pay_finish_btn(self):
        """点击支付完成按钮"""
        self.find_element(*self.pay_finish_btn, secs=20).click()

    @logged
    def is_pwd_input_dialog(self):
        """是否弹出密码输入框"""
        return self.is_element(*self.forget_pwd)

    @logged
    def click_forget_pwd_in_dialog(self):
        """密码输入框点击忘记密码"""
        self.find_element(*self.forget_pwd).click()

    @logged
    def input_pay_password(self, password='333333'):
        """输入支付密码"""
        pwd_view = self.find_element(*self.password_keyboard)
        location = pwd_view.location
        el_size = pwd_view.size  # p30 {'height': 732, 'width': 1080}
        logger.info("单位坐标：size:{}".format(el_size))
        unit_btn_width = el_size['width'] / 3 / 2
        unit_btn_height = el_size['height'] / 4 / 2
        for n in password:
            if int(n) == 0:
                excursion_x = unit_btn_width * 3
                excursion_y = unit_btn_height * 7
            elif 0 < int(n) <= 3:
                excursion_x = unit_btn_width * (2 * int(n) - 1)
                excursion_y = unit_btn_height
            elif 3 < int(n) <= 6:
                excursion_x = unit_btn_width * (2 * int(n) - 1)
                excursion_y = unit_btn_height * 3
            elif 6 < int(n) <= 9:
                excursion_x = unit_btn_width * (2 * int(n) - 1)
                excursion_y = unit_btn_height * 5
            else:
                excursion_x = unit_btn_width * 5
                excursion_y = unit_btn_height * 7
            self.tap_([(excursion_x + location['x'], excursion_y + location['y'])])
            logger.info("正在输入交易密码：{}, 坐标：{}".format(n, (excursion_x + location['x'], excursion_y + location['y'])))
        return True

    @logged
    def get_straight_down_text(self) -> float:
        """
        获取直降金额
        :return 负数
        """
        text = self.find_element(*self.straight_down).get_attribute('text').replace(' ¥', '')
        return float(text)

    @logged
    def get_input_money_text(self) -> float:
        """获取输入金额"""
        text = self.find_element(*self.input_money_text).get_attribute('text').replace('¥', '')
        return float(text)

    @logged
    def get_oil_no_text(self):
        """获取油号"""
        text = self.find_element(*self.oil_no_text).get_attribute('text')
        return text

    @logged
    def get_gun_no_text(self):
        """获取枪号"""
        text = self.find_element(*self.gun_no_text).get_attribute('text')
        return text

    @logged
    def get_selected_coupon_text(self) -> float:
        """
        获取已选择优惠券金额
        :return 负数
        """
        text = self.find_element(*self.coupon_selected).get_attribute('text').replace(' ¥')
        return float(text)

    @logged
    def click_select_coupon_btn(self):
        """点击优惠券选择"""
        self.find_element(*self.coupon_selected).click()

    @logged
    def click_select_coupon_card(self, index=0):
        """点击优惠券选择页中的第index个优惠券"""
        if self.find_elements(*self.coupon_card):
            self.find_elements(*self.coupon_card)[index].click()
        else:
            logger.info("收银台页面，没有可用优惠券～")

    @logged
    def click_no_use_coupon(self):
        """点击不实用优惠券"""
        self.find_element(*self.no_use_coupon).click()

    @logged
    def click_plus_vip_btn(self):
        """点击plus会员"""
        self.find_element(*self.puls_vip_btn)

    @logged
    def get_red_package_text(self) -> float:
        """获取红包金额"""
        text = self.find_element(*self.red_package_default).get_attribute('text')
        return float(text)

    @logged
    def click_red_package_in_page(self, index=1):
        """红包选择页点击红包"""
        red_package = (self.red_package[0], self.red_package[1].format(index))
        self.find_element(*red_package).click()

    @logged
    def get_available_balance_text(self) -> float:
        """获取可用余额"""
        if self.find_element(*self.available_balance).get_attribute('text'):
            text = self.find_element(*self.available_balance).get_attribute('text').replace('¥', '')
            return float(text)

    @logged
    def click_balance_btn(self):
        """点击余额支付"""
        self.find_element(*self.balance_pay_btn).click()

    @logged
    def click_other_pay_btn(self, other_pay='alipay'):
        """点击其他支付"""
        if other_pay == 'alipay':
            index = 0
        elif other_pay == 'wechat':
            index = 1
        elif other_pay == 'cloud':
            index = 2
        elif other_pay == 'jdpay':
            index = 3
        else:
            raise NotImplementedError("还没实现该支付方式: {}".format(other_pay))
        self.find_elements(*self.other_pay_btn)[index].click()

    @logged
    def get_total_money_text(self) -> float:
        """获取合计支付金额"""
        text = self.find_element(*self.total_money).get_attribute('text')
        return float(text)

    @logged
    def get_money_with_wechat_pay(self) -> float:
        """获取微信支付页面的支付金额"""
        text = self.find_element(*self.wechat_pay_money).get_attribute('text')
        return float(text)

    @logged
    def is_set_pwd_dialog(self):
        """是否显示设置密码弹窗"""
        if self.find_element(*self.set_password_dialog_message):
            self.find_element(*self.password_dialog_right).click()
            return True
        else:
            logger.info("没弹出设置交易密码～")
            return False

    @logged
    def click_set_password_dialog(self, switch=True):
        """点击设置支付密码"""
        if switch:
            if self.find_element(*self.password_dialog_right):
                self.find_element(*self.password_dialog_right).click()
        else:
            if self.find_element(*self.password_dialog_right):
                self.find_element(*self.password_dialog_cancel).click()

    @logged
    def is_cancel_dialog(self):
        """取消支付按钮弹窗"""
        return self.find_element(*self.cancel_dialog)

    @logged
    def click_cancel_dialog(self, switch=True):
        """取消支付按钮处理"""
        if switch:
            self.find_element(*self.cancel_dialog_quit_btn).click()
        else:
            self.find_element(*self.cancel_dialog_continue).click()
