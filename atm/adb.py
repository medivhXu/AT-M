#!/usr/bin/env python3

from atm.log import LOGGER,logged
from super_classes.commond import Command
from exceptions.environment import AdbEnvironmentException


class Adb(Command):
    def __init__(self):
        super(Adb, self).__init__()

    def _check_adb(self):
        r = self.run_cmd('adb')
        if not len(r):
            raise AdbEnvironmentException("adb 环境错误！")
        return True

    def check_port(self, port):
        pass

    def start_appium(self, add, port, bootstrap_port, chrome_port, udid):
        pass

    def show_sdk(self):
        pass

    def kill_port(self, port):
        pass

    def connect(self, ip='127.0.0.1', port=4727):
        if self._check_adb():
            r = self.run_cmd('adb connect {}:{}'.format(ip, port))
            if len(r):
                return True
            else:
                return False

    def disconnect(self, ip='127.0.0.1'):
        if self._check_adb():
            r = self.run_cmd('adb disconnect {}'.format(ip))



    def get_devices_version(self):
        pass

    def get_devices_name(self):
        pass

    def get_package_name(self):
        pass
