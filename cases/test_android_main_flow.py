#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: test_android.py
@time: 2020-02-27 12:22
"""

import sys

from base import *
from base.runner import TestRunner
from module import *

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class TestAndroid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        platform, cls.platform_version = auto_set_device_info()
        cls.driver = conn(platform=platform)

        cls.advertising = Advertising(cls.driver)
        cls.check_stand = CheckStand(cls.driver)
        cls.first_page = FirstPage(cls.driver)
        cls.gas_info = GasInfo(cls.driver)
        cls.gas_list = GasList(cls.driver)
        cls.login = Login(cls.driver)
        cls.order = Order(cls.driver)
        cls.order_finished = OrderFinished(cls.driver)
        cls.person_center = PersonCenter(cls.driver)
        cls.set_pay_pwd = SetPayPassword(cls.driver)
        cls.setting = Setting(cls.driver)

    def setUp(self):
        self.env = CONF.read()['MYSQL']
        self.phone, self.info = get_user_info_from_conf()

    def tearDown(self):
        # self.person_center.click_setting_btn()
        # self.setting.click_logout_btn()
        self.driver.quit()
        del self.phone
        del self.info
        del self.env

    def test_main_flow(self):
        # if reset_local_phone_login_flow(self):  # 仅真机有sim卡使用
        if reset_other_login_flow(self):  # 通用-必须连接VPN
            logger.info("登录成功")
        else:
            logger.info("登录失败～")
        self.first_page.click_immediately_add_oil()
        self.gas_info.click_gun_no()
        input_money = self.info.get('input_money')
        self.gas_info.input_money(input_money)
        self.gas_info.click_next_btn()
        self.gas_info.click_continue_next_btn()
        available_balance = self.check_stand.get_available_balance_text()
        if available_balance < input_money:
            user_id = get_user_id_by_phone(self.phone, **self.env)
            set_account(user_id=user_id, balance=input_money, **self.env)
            self.check_stand.press_keycode_by_android(AndroidKeyCodeEnum.BACK.value)
            if self.check_stand.is_cancel_dialog():
                self.check_stand.click_cancel_dialog()
                self.gas_info.click_next_btn()
                self.gas_info.click_continue_next_btn()
        self.check_stand.click_pay_finish_btn()
        if self.check_stand.is_set_pwd_dialog():
            set_pwd_flow(self)
        if self.check_stand.is_pwd_input_dialog():
            self.check_stand.input_pay_password()
        if self.order_finished.is_ad_window():
            self.order_finished.click_ad_close_btn()
        self.assertTrue((self.order_finished.get_order_finished_status_text()
                         and self.order_finished.get_refund_btn_text()))


if __name__ == '__main__':
    logger.add('../logs/UIT.log', rotation='50 MB', retention='10 days', level='INFO', encoding='utf-8')
    email_conf = conf_load('__conf.yaml')
    emails = email_conf.read().get('EMAIL').get('recipients')
    TestRunner('./', 'Android UI自动化测试', '测试环境', '{}'.format(emails[0].split('@')[0])).run()
