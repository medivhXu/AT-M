#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: start.py
@time: 2020-03-04 21:27
"""

from base.runner import *

if __name__ == '__main__':
    logger.add('logs/UIT.log', rotation='500 MB', retention='10 days')
    email_conf = conf_load('__conf.yaml')
    emails = email_conf.read().get('EMAIL').get('recipients')
    run = TestRunner('./', 'Android UI自动化测试', '测试环境', '{}'.format(emails[0].split('@')[0])).run()
