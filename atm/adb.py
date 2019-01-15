#!/usr/bin/env python3
import re
import os

from atm.log import LOGGER, logged
from super_classes.commond import Command
from exceptions.myexception import AdbConnectException


class Adb(Command):
    """
    Android sdk adb 命令管理
    """
    def __init__(self):
        super(Adb, self).__init__()
        self._tool_path = self._add_android_path()
        self._adb = os.path.join(self._tool_path, 'adb')
        self._aapt = os.path.join(self._tool_path, 'aapt')

    @logged
    def start(self):
        """启动adb server"""
        if self._tool_path:
            self.run_cmd('{} start-server'.format(self._adb))

    @logged
    def stop(self):
        """停止adb server"""
        self.run_cmd('{} kill-server'.format(self._adb))

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
                r = self.run_cmd('{} connect {}:{}'.format(self._adb, ip, port))
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
        """断开设备连接"""
        if ip:
            self.run_cmd('{} disconnect {}'.format(self._adb, ip))
        else:
            self.kill_port()

    @logged
    def get_package_main_activity(self, package_fp):
        """
        获取 apk 的 launch activity
        :param package_fp: app文件地址
        :return: str(main activity)
        """
        r = self.run_cmd('{} dump badging {}'.format(self._aapt, package_fp))
        activities = [el.decode() for el in r if re.search('launchable-activity: name=[\'].+?[\']', el.decode())]
        activity = activities[0].split('\'')[1]
        return activity

    @logged
    def get_package_name(self, packages_fp):
        """
        获取apk包名
        :param packages_fp: apk文件地址
        :return: type(str)
        """
        r = self.run_cmd('{} d permissions {}'.format(self._aapt, packages_fp))
        if not len(r):
            r = self.run_cmd('{} d permissions {}'.format(self._aapt, packages_fp))
            return r[0].decode().split(': ')[1]
        else:
            return r[0].decode().split(': ')[1]

    @staticmethod
    @logged
    def _add_android_path(env_name='APPIUM_TOOLS'):
        """
        把atm自带adb和aapt工具添加到系统环境变量中
        :param env_name: 环境变量key name
        :return:
        """
        if env_name not in os.environ.keys():
            __dir__ = os.path.dirname(os.path.abspath(__file__))
            tools_path = os.path.join(__dir__, '../tool/')
            os.environ[env_name] = tools_path
            return tools_path
        else:
            LOGGER.info("系统有atm.tools环境变量～")
            return os.environ.get(env_name)
