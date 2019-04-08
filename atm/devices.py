# !/uer/bin/env python3

from atm.super_classes.devices_abstract import Devices
from atm.log import logged
from atm.adb import Adb
from atm.imobile import IMobile
from atm.apps import Apps


class Android(Devices):
    @logged
    def __init__(self, ip=None, port=None):
        super(Android, self).__init__()
        self._ip = ip
        self._port = port
        self.adb_cls = Adb()
        self.apk = Apps(self.__class__.__name__)
        self._devices_info = {}
        self._device_info = {}
        self._device_name = None

    def start_appium(self):
        pass

    def connect(self):
        if self._ip:
            self.adb_cls.connect(self._ip, self._port)
            return self.get_device_info()
        else:
            return self.get_device_info()

    def get_devices_info(self):
        self._devices_info[self._device_name] = self._device_info
        return self._devices_info

    @logged
    def disconnect(self):
        self.adb_cls.disconnect(self._ip)

    def get_device_info(self):
        device_info_byte = self.adb_cls.run_cmd('{} shell getprop'.format(self.adb_cls.adb))
        dic = {}
        for i in device_info_byte:
            line = i.decode().strip().split(':')
            if line[0] != ']':
                dic[line[0].strip()[1:-1]] = line[1].strip()[1:-1]
        self._device_name = dic.get('ro.product.model')
        device_info = {self._device_name: {'platformversion': dic.get('ro.build.version.release'),
                                           'devicename': dic.get('ro.serialno'),
                                           'automationname': 'Appium',
                                           'unicodekeyboard': True,
                                           'resetkeyboard': True,
                                           'noreset': True,
                                           }}
        return device_info


class Ios(Devices):
    @logged
    def __init__(self):
        super(Ios, self).__init__()
        self._imobile = IMobile()
        self.udid = None

    def connect(self):
        pass

    @logged
    def get_devices_info(self):
        pass

    @logged
    def disconnect(self):
        pass


class IosSimulator(Devices):
    @logged
    def __init__(self):
        super(IosSimulator, self).__init__()
        self._libimobile = IMobile()

    def connect(self):
        pass

    @logged
    def disconnect(self, ip=None):
        pass

    @logged
    def get_devices_info(self):
        pass


class AndroidSimulator(Devices):
    def __init__(self):
        super(AndroidSimulator, self).__init__()

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_devices_info(self):
        pass


if __name__ == '__main__':
    run = Android()
    print(run.get_device_info())
