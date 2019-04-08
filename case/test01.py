#!/usr/bin/env python3

import os
import sys
import unittest
from parameterized import parameterized
from atm import *
from atm.log import LOGGER

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class MainProcess(unittest.TestCase, element_finder.MobileDriver):
    @classmethod
    def setUpClass(cls):
        cls.driver = apper.Apper()
        # 用例开始数据准备

    @classmethod
    def tearDownClass(cls):
        # 用例结束数据清理
        del cls.par

    # run data
    # par = xlsx_manage.XLSXData().get_case_data()

    # debug data
    par = [(1, 10066001, 13800138000, True, False, 'amount', 123456, 92, 'my gas', 1, 100, True, '好', False, 1,
            '/img/img.png')]

    @parameterized.expand(input=par)
    def test_ios_main(self, no, phone, platform_code, business_prefix, login, pay_op, pwd, gas_no, gas_name,
                      gun_no, money, use_coupons, thumbs_up, comments, certification_opt, certification_img_path):
        """
        测试车主邦app正常流程
        :param no: 用例编号
        :param phone: 用户手机号
        :param platform_code: 平台编号
        :param business_prefix: 是否跳过开屏广告、新手引导、首页弹窗广告
        :param login: 是否需要登录
        :param pay_op: 支付方式
        :param pwd: 支付密码
        :param gas_no: 油号
        :param gas_name: 油站名称
        :param gun_no: 枪号
        :param money: 金额
        :param use_coupons: 是否使用优惠券
        :param thumbs_up: 是否点赞
        :param comments: 评论内容
        :param certification_opt: 认证类型
        :param certification_img_path: 认证图片路径
        :return: nothing
        """

        LOGGER.info("正在执行用例:{}".format(no))

        # 主流程数据准备
        set_database.check_litre_at_checkstand_by_ios(phone, platform_code)
        set_certification_of_car.set_certification_of_car_by_ios(phone, certification_opt, certification_img_path)

        if business_prefix is True:  # 业务前缀开关
            self.compel_waiting(3)  # 这等了3秒广告
            start_prefix.ios_start_prefix(self)
        else:
            pass  # 处理业务前缀逻辑

        if login is True:  # 登录开关
            login_and_logout.phone_login_by_ios(self, phone)
        else:
            pass  # 处理未登录用例

        if gas_no == 'default':
            # 查找首页默认油号，还没写
            LOGGER.info("默认油号为：{}".format(gas_no))
        else:
            gas_no_finder_form_gas_list.set_gas_no_at_first_page_by_ios(self, gas_no)

        # 找到油站并进入输入金额页
        if gas_name_finder_from_gas_list.find_and_click_gas_name_at_page_by_ios(self=self, gas_name=gas_name,
                                                                                max_page_no=3):
            raise my_exception.MyException("未找到油站")

        self.find_accessibility_id("付油费").click()
        if self.find_element_by_ios_predicate_("name == '继续支付'"):
            self.find_element_by_ios_predicate_('name == "继续支付"').click()
        self.find_element_by_ios_predicate_("name == '{}号枪'".format(gun_no)).click()
        amount_input = self.find_element_by_ios_predicate_("type == 'XCUIElementTypeTextField'")
        amount_input.clear()
        amount_input.send_keys(money)
        self.driver.find_element_by_ios_predicate("name == '确定'").click()

        check_litre.check_litre_at_checkstand_by_ios(self)

        if use_coupons is True:
            check_use_coupons.check_use_coupons_by_ios(self)

        else:
            a = self.find_elements_by_ios_predicate_("type == 'XCUIElementTypeStaticText' AND 'name' LIKE '.*元'").text()
            LOGGER.info("检测直降价格{}".format(a))
            check_straight_down.check_straight_down_by_ios(self)

        if pay_op == 'amount':
            LOGGER.info("---余额支付---")
            if self.find_element_by_ios_predicate_("name == 'pay-option-selected'").is_selected():
                pass
            else:
                self.find_element_by_ios_predicate_("name == 'pay-option-selected'").click()
                if not self.find_element_by_ios_predicate_("name == 'pay-option-selected'").is_selected():
                    LOGGER.warning("余额不足！或超过当日限额！")
                    self.assertTrue("余额支付失败", "余额不足！或超过当日限额！")

            self.find_elements_by_ios_predicate_("type == 'XCUIElementTypeOthe'")[0].click()
            if self.find_element_by_ios_predicate_("name == '设置'"):
                self.find_element_by_ios_predicate_("name == '设置'").click()
                self.find_element_by_ios_predicate_("name == '获取验证码'").click()
                msg = get_msg_info_from_db.GetMsgInfo().get_password_msg(phone)
                self.find_elements_by_ios_predicate_("type == 'XCUIElementTypeTextField'")[1].send_keys(msg)
                pwd_input = self.find_elements_by_ios_predicate_("type == 'XCUIElementTypeSecureTextField'")
                pwd_input[0].send_keys(pwd)
                pwd_input[1].send_keys(pwd)
                self.find_element_by_ios_predicate_("name == '确定'").click()
            for i in pwd:
                self.find_elements_by_ios_predicate_("type == 'XCUIElementTypeOthe'")[pwd.index(i)].send_keys(i)
            self.find_element_by_ios_predicate_("name == '去支付'").click()

            set_thumbs_and_comments.set_thumbs_and_comments_by_ios(self, thumbs_up, comments)

        elif pay_op == 'wechart':
            LOGGER.info("---微信支付---")
            if self.find_element_by_ios_predicate_('name == "pay-option-selected"').is_selected():
                self.find_element_by_ios_predicate_('name == "pay-option-selected"').click()
            self.find_element_by_ios_predicate_('name == "去支付"').click()
            if self.find_element_by_ios_predicate_('name == "微信支付"').is_selected():
                pass
            else:
                self.find_element_by_ios_predicate_('name == "微信支付"').click()
            self.find_element_by_ios_predicate_('name == "确定支付"').click()
            if self.driver.switch_to_alert.text():
                self.assertIn("安装微信", self.driver.switch_to_alert.text(), "没安装微信，支付失败!")
            else:
                pass
                # 微信未登录

        elif pay_op == 'alipay':
            LOGGER.info("---支付宝支付---")
            if self.find_element_by_ios_predicate_('name == "pay-option-selected"').is_selected():
                self.find_element_by_ios_predicate_('name == "pay-option-selected"').click()
            self.find_element_by_ios_predicate_('name == "去支付"').click()
            if self.find_element_by_ios_predicate_('name == "支付宝支付"').is_selected():
                pass
            else:
                self.find_element_by_ios_predicate_('name == "支付宝支付"').click()
            self.find_element_by_ios_predicate_('name == "确定支付"').click()
            # 吊起支付宝h5或吊起支付宝网页

        elif pay_op == 'jdpay':
            LOGGER.info("---京东支付----")
            if self.find_element_by_ios_predicate_('name == "pay-option-selected"').is_selected():
                self.find_element_by_ios_predicate_('name == "pay-option-selected"').click()
            self.find_element_by_ios_predicate_('name == "去支付"').click()
            if self.find_element_by_ios_predicate_('name == "京东支付"').is_selected():
                pass
            else:
                self.find_element_by_ios_predicate_('name == "京东支付"').click()
            self.find_element_by_ios_predicate_('name == "确定支付"').click()
            # 吊起京东app或吊起京东网页

        else:
            raise my_exception.MyException("****未知支付方式****")
        self.compel_waiting(1)
        self.quit_()


if __name__ == '__main__':
    run = runner.TestRunner('./', '车主邦测试用例', '测试环境：{}', 'Medivh'.format("ios"))
    run.debug()

'''
说明：
'./' ： 指定测试目录。
'百度测试用例' ： 指定测试项目标题。
'测试环境：android' ： 指定测试环境描述(注：这里的设备是自动获取，请填写准确)。
'Medivh': 测试人员

debug() # debug模式不生成测试报告
run()   # run模式生成测试报告
'''
