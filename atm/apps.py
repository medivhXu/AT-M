#!/usr/bin/env python3
import os
import re

from atm.log import LOGGER, logged
from atm.adb import Adb
from exceptions.myexception import *


class Apk:
    def __init__(self, app_dir_name='../packages/', apk_version=None):
        __dir__ = os.path.dirname(os.path.abspath(__file__))
        self._file_path = os.path.join(__dir__, app_dir_name)
        self._adb = Adb()
        self.version = apk_version
        self._num = 0
        self.package_name = None
        self.main_activity = None
        self.apk_path = None

    def get_package_path(self):
        apps = os.listdir(self._file_path)
        if len(apps):
            for app in apps:
                if self.version:
                    apks = re.findall(re.compile('.*{}.*.apk'.format(self.version), re.S), app)
                    if len(apks):
                        for apk in apks:
                            yield os.path.join(self._file_path, apk)
                    else:
                        raise ApkFileNotFoundException("没找到任何apk文件!")

                else:
                    apks = [a for a in apps if re.findall(re.compile('.*.apk', re.S), a)]
                    if len(apks):
                        for apk in apks:
                            yield os.path.join(self._file_path, apk)
                    else:
                        LOGGER.warning('没找到apk文件!')
                        return False
        else:
            raise ApkFileNotFoundException("没找到任何apk文件!")

    @property
    def get_package_name(self):
        for package in self.get_package_path():
            self._num += 1
        package_name = self._adb.get_package_name()
        return package_name

    @property
    def get_main_activity(self):
        main_activity = self._adb.get_package_main_activity(self.get_package_path().__next__())
        return main_activity


if __name__ == '__main__':
    apk1 = Apk()
    print(apk1.get_package_path().__next__())
