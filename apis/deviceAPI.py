# ！/usr/bin/env python3

from super_classes.devices_abstract import Android, Ios


class Device(object):
    def __init__(self, devices):
        if isinstance(devices, tuple):
            self.devices = list(map(lambda x: str(x).capitalize(), devices))
        else:
            raise TypeError('{}参数必须是个元组类型')

    def get_device_info(self):
        for device in self.devices:
            if len(device):
                return eval(device)().get_device_info()
            else:
                pass

    def get_package_name(self):
        for device in self.devices:
            if len(device):
                return eval(device)().get_package_name()
