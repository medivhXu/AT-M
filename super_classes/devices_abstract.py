# !/uer/bin/env python3

import abc


class Devices(metaclass=abc.ABCMeta):
    """测试设备鸡肋"""
    @abc.abstractmethod
    def get_devices_info(self):
        raise NotImplementedError

    @abc.abstractmethod
    def disconnect(self):
        raise NotImplementedError

    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError
