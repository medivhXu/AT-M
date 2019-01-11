# !/uer/bin/env python3

from atm.log import LOGGER, logged
from super_classes.devices_abstract import *
from atm.adb import Adb
from atm.imobile import IMobile
from atm.apps import Apk
from exceptions.myexception import *


class Android(Devices):
    @logged
    def __init__(self, ip, port):
        super(Android, self).__init__()
        self._ip = ip
        self._port = port
        self.adb = Adb()
        self._device_name = None
        self.apk = Apk()
        self._device_info = {}

    def start_appium(self):
        self.adb.start_appium(udid=self.get_devices_name_dict())

    def connect(self):
        if self._ip:
            self.adb.connect(self._ip, self._port)
            return self.get_devices_name_dict()
        else:
            return self.get_devices_name_dict()

    @logged
    def disconnect(self):
        self.adb.disconnect(self._ip)

    def get_devices_version(self):
        r = self.adb.run_cmd('{} shell getprop ro.build.version.release'.format(self.adb.adb_path))
        return r[0].decode()

    def get_devices_name_dict(self):
        r = self.adb.run_cmd('{} devices'.format(self.adb.adb_path))
        device_list = [d.decode() for d in r[1:] if d != b'\n']
        device_dict = {}
        d1 = [dev_.split() for dev_ in device_list]
        device = {}
        for i in d1:
            if i[1] == 'unauthorized':
                LOGGER.warning('[-]设备：设备首次接入，请手动授权调试！')
                raise AdbEnvironmentException("[-]设备：设备首次接入，请手动授权调试！")
            elif i[1] == 'offline':
                raise AdbConnectException("不能连接设备，请在开发者选项中打开usb调试～")
            elif i[1] == 'no permissions':
                raise AdbEnvironmentException("请检查adb环境！参考网站https://blog.csdn.net/binglumeng/article/details/69525361")
            else:
                device_dict[i[1]] = i[0]
        device.update(zip([j + 1 for j in range(len(device_dict))], device_dict.items()))
        return device


class Ios(Devices):
    @logged
    def __init__(self):
        super(Ios, self).__init__()
        self._imobile = IMobile()
        self.udid = None

    def connect(self):
        pass

    @logged
    def get_devices_info(self, device_name):
        pass

    @logged
    def disconnect(self, udid):
        pass


class IosSimulator(Devices):
    @logged
    def __init__(self):
        super(IosSimulator, self).__init__()
        self._libimobile = IMobile()

    @logged
    def disconnect(self, ip=None):
        pass

    @logged
    def get_devices_info(self, device_name):
        pass


class AndroidSimulator(Devices):
    pass
