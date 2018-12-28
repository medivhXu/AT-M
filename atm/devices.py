# !/uer/bin/env python3

import subprocess
import os
import re
from atm.log import LOGGER, logged
from super_classes.devices_abstract import *
from atm.adb import Adb

__dir__ = os.path.dirname(os.path.abspath(__file__))


class Android(Devices):
    def __init__(self):
        super(Android, self).__init__()
        self._adb = Adb()
        self.ip = None
        self.port = None

    def connect(self):
        a = self._adb.connect(self.ip, self.port)
        return a or False

    def get_device_info(self):
        pass

    def disconnect(self):
        self._adb.disconnect(self.ip, self.port)


class Ios(Devices):
    def __init__(self):
        super(Ios, self).__init__()
        self._libimobile = Instruments()

    def connect(self):
        a = self._libimobile.connect()
        return a or False

    def get_device_info(self):
        pass

    def disconnect(self):
        pass
