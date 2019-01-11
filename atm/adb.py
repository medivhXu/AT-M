#!/usr/bin/env python3
import re
import os

from atm.log import LOGGER, logged
from super_classes.commond import Command
from exceptions.myexception import AdbEnvironmentException, AdbConnectException


class Adb(Command):
    """
    Android sdk adb 命令管理
    """
    def __init__(self):
        super(Adb, self).__init__()
        self.tool_path = self._add_android_path()
        if self.tool_path:
            self.adb_path = os.path.join(self.tool_path, 'adb')
            self.aapt_path = os.path.join(self.tool_path, 'aapt')
        else:
            LOGGER.error("tools文件有问题～！")
            raise AdbEnvironmentException("环境错误！")

    @logged
    def start(self):
        """启动adb server"""
        if self.tool_path:
            self.run_cmd('{} start-server'.format(self.adb_path))

    @logged
    def stop(self):
        """停止adb server"""
        self.run_cmd('{} kill-server'.format(self.adb_path))

    @logged
    def connect(self, ip=None, port=5555):
        """
        连接设备
        :param ip: 需要连接的设备ip
        :param port: 连接设备的端口
        :return:
        """
        if ip:
            if port:
                r = self.run_cmd('{} connect {}:{}'.format(self.adb_path, ip, port))
                LOGGER.info('adb WIFI连接返回结果：{}'.format(r))
                for el in r:
                    if re.search('failed.*', el.decode()):
                        raise AdbConnectException('不能连接设备，请在开发者选项中打开usb调试～')
                    elif re.search('already.*', el.decode()):
                        return True
                    else:
                        LOGGER.info("adb 连接返回不明，返回结果:{}, ***赶紧扩展***".format(r))
                        return False
        else:
            LOGGER.info("Android设备通过usb连接！")

    @logged
    def disconnect(self, ip=None):
        if ip:
            self.run_cmd('{} disconnect {}'.format(self.adb_path, ip))
        else:
            self.kill_port()

    @logged
    def get_package_main_activity(self, package_fp):
        r = self.run_cmd('{} dump badging {}'.format(self.aapt_path, package_fp))
        activities = [el.decode() for el in r if re.search('launchable-activity: name=[\'].+?[\']', el.decode())]
        activity = activities[0].split('\'')[1]
        return activity

    @logged
    def get_package_name(self, packages_fp):
        r = self.run_cmd('{} d permissions {}'.format(self.aapt_path, packages_fp))
        if not len(r):
            r = self.run_cmd('{} d permissions {}'.format(self.aapt_path, packages_fp))
            return r[0].decode().split(': ')[1]
        else:
            return r[0].decode().split(': ')[1]

    @staticmethod
    @logged
    def _add_android_path(env_name='APPIUM_TOOLS'):
        if env_name not in os.environ.keys():
            __dir__ = os.path.dirname(os.path.abspath(__file__))
            aapt_path = os.path.join(__dir__, '../tool/')
            os.environ[env_name] = aapt_path
            return aapt_path
        else:
            return False
