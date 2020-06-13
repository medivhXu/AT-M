#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: runner.py
@time: 2020-03-04 21:27
"""


import datetime
import os
import unittest

from base import HTMLTestReportCN
from base.send_email import smtp_email
from config_loader import conf_load
from loguru import logger


class TestRunner(object):
    @logger.catch
    def __init__(self, cases="./", title="CZB Test Report", description="Test case execution",
                 tester="system"):
        self.cases = cases
        self.title = title
        self.des = description
        self.tester = tester

    @logger.catch
    def run(self, receivers=None):

        for filename in os.listdir(self.cases):
            if filename == "report":
                break
        else:
            os.mkdir(self.cases + '/report')

        now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        report = os.path.join(os.path.dirname(os.path.abspath(__file__)), now.join(("../report/", ".html")))
        with open(report, 'wb') as fp:
            tests = unittest.defaultTestLoader.discover(self.cases, pattern='test*.py', top_level_dir=None)
            runner = HTMLTestReportCN.HTMLTestReportCN(stream=fp, title=self.title, description=self.des,
                                                       tester=self.tester)
            try:
                runner.run(tests)
            except ConnectionRefusedError:
                logger.error("没打开Appium Desktop APP~")

        log_dp = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs')
        log_fp = os.path.join(log_dp, 'UIT.log')
        report_html = open(report).read() + '\n'
        email_dict = conf_load('../__conf.yaml').read()['EMAIL']
        if receivers:
            smtp_email(sender=email_dict['sender'], receivers=receivers, password=email_dict['password'],
                       smtp_server=email_dict['smtp_server'], port=email_dict['port'], html=report_html,
                       attachment=[report, log_fp])
        else:
            smtp_email(sender=email_dict['sender'], receivers=email_dict['recipients'], password=email_dict['password'],
                       smtp_server=email_dict['smtp_server'], port=email_dict['port'], html=report_html,
                       attachment=[report, log_fp])
        logger.info("邮件已发送！")

    @logger.catch
    def debug(self):
        tests = unittest.defaultTestLoader.discover(self.cases, pattern='test*.py', top_level_dir=None)
        runner = unittest.TextTestRunner(verbosity=2)
        print("test start:")
        runner.run(tests)
        print("test end!!!")
