#!/usr/bin/env python3

"""
@author: Medivh Xu
@file: adb_kit.py
@time: 2020-03-20 14:10
"""

import re
import os

from loguru import logger
from base.kit.command import Command
from base.my_exception import AdbConnectException, DevicePermissionsException


class Adb(Command):
    """
    Android sdk adb 命令管理
    """

    def __init__(self):
        super(Adb, self).__init__()
        self._tool_path = self._add_android_path()
        self.adb_path = os.path.join(self._tool_path, 'adb')
        self.aapt_path = os.path.join(self._tool_path, 'aapt')

    def start(self):
        """启动adb server"""
        if self._tool_path:
            self.run_cmd('{} start-server'.format(self.adb_path))

    def stop(self):
        """停止adb server"""
        self.run_cmd('{} kill-server'.format(self.adb_path))

    def connect(self, ip=None, port=5555):
        """
        连接设备
        :param ip: 需要连接的设备ip
        :param port: 连接设备的端口
        :return:
        """
        if ip:
            r = self.run_cmd('{} connect {}:{}'.format(self.adb_path, ip, port))
            logger.info('adb WIFI连接返回结果：{}'.format(r))
            for el in r:
                if re.search('failed.*', el.decode()):
                    raise AdbConnectException('不能连接设备，请在开发者选项中打开usb调试～')
                elif re.search('already.*', el.decode()):
                    return True
                else:
                    logger.info("adb 连接返回不明，返回结果:{}, ***赶紧扩展***".format(r))
                    return False
        else:
            logger.info("Android设备通过usb连接！")
            res = self.run_cmd('{} devices'.format(self.adb_path))
            devices = {}
            for index, el in enumerate(res):
                if index >= 1:
                    if 'offline' in el.decode():
                        logger.warning("设备已离线！设备名称：{}".format(el.decode().replace('\n', '').split('\t')))
                    elif 'un' in el.decode():
                        logger.warning("设备未授权！设备名称：{}".format(el.decode().replace('\n', '').split('\t')))
                    else:
                        device_name_list = el.decode().replace('\n', '').split('\t')
                        if len(device_name_list) == 2:
                            devices[index] = device_name_list[0]
            return devices

    def disconnect(self, ip=None):
        """断开设备连接"""
        if ip:
            self.run_cmd('{} disconnect {}'.format(self.adb_path, ip))
        else:
            self.kill_port(self.get_pid_by_keyword('adb'))

    def get_package_main_activity_by_path(self, package_fp):
        """
        获取 apk 的 launch activity
        :param package_fp: app文件地址
        :return: str(main activity)
        """
        r = self.run_cmd('{} dump badging {}'.format(self.aapt_path, package_fp))
        if not r:
            logger.warning("apk包经过加固，不能取出activity！")
            return r or False
        activities = [el.decode() for el in r if re.search('launchable-activity: name=[\'].+?[\']', el.decode())]
        activity = activities[0].split('\'')[1]
        return activity

    def get_package_name_by_path(self, packages_fp):
        """
        获取apk包名
        :param packages_fp: apk文件地址
        :return: type(str)
        """
        r = self.run_cmd('{} d permissions {}'.format(self.aapt_path, packages_fp))
        if not len(r):
            logger.warning("没取出包名，apk加固了！")
        return r or False

    @staticmethod
    def _add_android_path(env_name='APPIUM_TOOLS'):
        """
        把atm自带adb和aapt工具添加到系统环境变量中
        :param env_name: 环境变量key name
        :return:
        """
        if env_name not in os.environ.keys():
            __dir__ = os.path.dirname(os.path.abspath(__file__))
            tools_path = os.path.join(__dir__, '../../tool/')
            os.environ[env_name] = tools_path
            return tools_path
        else:
            logger.info("系统有tools环境变量～")
            return os.environ.get(env_name)
