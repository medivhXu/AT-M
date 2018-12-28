# !/uer/bin/env python3

import abc


class Devices(metaclass=abc.ABCMeta):
    def __init__(self):
        self.device_name = None
        self.platform_version = None

    @abc.abstractmethod
    def get_device_info(self):
        raise NotImplementedError

    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError

    @abc.abstractmethod
    def disconnect(self):
        raise NotImplementedError
