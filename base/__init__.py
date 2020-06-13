#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: __init__.py
@time: 2020-02-27 12:33
"""

__author__ = "Medivh Xu"

__version__ = "1.1.0"

__email__ = "medivh_xu@outlook.com"

from appium import webdriver

from base.logged import logged, logger
from base.devices_manager import Android, Ios
from base.kit.adb_kit import Adb
from base.kit.command import Command
from base.android_keycode_enum import AndroidKeyCodeEnum
from config_loader import conf_load
from base.my_exception import *


CONF = conf_load('../__conf.yaml')


@logged
def conn(platform=None, ip=None, port=None):
    """连接webdriver"""
    platform_dict = {'Android': Android, 'Ios': Ios}
    if str(platform).capitalize() in platform_dict:
        platform_dict.get(platform)(ip=ip, port=port)
        return webdriver.Remote(CONF.read()['URL'], desired_capabilities=CONF.read().get(str(platform).upper()))
    else:
        raise NotImplementedError("未实现该平台！目前只实现：{}".format(platform_dict.keys()))


@logged
def auto_set_device_info():
    """
    自动获取设备信息写到配置文件里
    :param
    :return:
    """

    num = 3
    while True:
        Adb().stop()
        adb_device = Adb().connect()
        if adb_device:
            if len(adb_device) == 1:
                devices_info = Android().get_device_info(adb_device.get(1))
                platform_version = str(devices_info.get('platformVersion'))
                if platform_version == '7.0':
                    appium_version = Command.check_appium_version()
                    if appium_version == '1.6.3' or appium_version == '1.6.4':
                        info = {"ANDROID": {"automationName": "UIAutomator2"}}
                        CONF.update(info)
                info = {"ANDROID": devices_info}
                CONF.update(info)
                logger.info("写入配置文件成功，参数为platformVersion:{},deviceName:{}".format(platform_version, devices_info))
                return 'Android', platform_version
            else:
                raise NotImplementedError("目前只支持一个设备连接～")
        else:
            logger.info('adb 重试～')
            num -= 1
            if num == 0:
                raise DeviceNotFoundException("没有可用设备！")
            continue
