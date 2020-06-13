# !/uer/bin/env python3
"""
@author: Medivh Xu
@file: deices_manager.py
@time: 2020-03-23 12:22
"""

from base.kit.adb_kit import Adb
from base.kit.imobile_kit import IMobile


class Android:
    def __init__(self, ip=None, port=None):
        """安卓设备、app等管理"""
        # TODO 检测设备app是否安装
        self._ip = ip
        self._port = port
        self.adb = Adb()
        self.adb.start()
        self._devices_info = {}

    def start_appium(self):
        self.adb.start_appium(addr=self._ip, udid=self._devices_info.get('device_name'))

    def disconnect(self):
        self.adb.disconnect(self._ip)

    def get_device_info(self, device_id):
        device_info_list = self.adb.run_cmd('{} -s {} shell getprop'.format(self.adb.adb_path, device_id))
        dic = {}
        for i in device_info_list:
            line = i.decode().strip().split(':')
            if line[0] != ']':
                try:
                    dic[line[0].strip()[1:-1]] = line[1].strip()[1:-1]
                except IndexError as e:
                    continue
        device_name_str = dic.get('ro.product.model')
        if device_name_str:
            device_info = {'platformVersion': dic.get('ro.build.version.release'),
                           'deviceName': self.adb.connect().get(1),
                           'platformName': self.__class__.__name__}
            return device_info
        else:
            raise RuntimeError("没找到设备！")

    def uninstall_app(self, package_name):
        res = self.adb.run_cmd('{} uninstall {}'.format(self.adb.adb_path, package_name))
        return res

    def install_app(self, apk_fp):
        res = self.adb.run_cmd('{} install {}'.format(self.adb.adb_path, apk_fp))
        return res


class Ios:
    def __init__(self):
        self._imobile = IMobile()
        self.udid = None

    def connect(self):
        pass

    def get_devices_info(self):
        pass

    def disconnect(self):
        pass
