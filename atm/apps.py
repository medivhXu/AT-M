#!/usr/bin/env python3
import os
import re

from atm.log import LOGGER, logged
from exceptions.myexception import *


class Apps:
    """app 包管理，主要用于自动读取app文件位置"""
    @logged
    def __init__(self, platform=None, app_dir_name='../packages/', apk_version=None, env='test'):
        __dir__ = os.path.dirname(os.path.abspath(__file__))
        self._file_dir_path = os.path.join(__dir__, app_dir_name)
        self._app_version = apk_version
        self._app_path = None
        self._app_name = None
        self._platform = str(platform).capitalize()
        self._env = env

    @property
    @logged
    def path(self):
        self._set_app()
        return str(self._app_path) or False

    @property
    @logged
    def name(self):
        self._set_app()
        self._app_name = str(self._app_path).split('/')[-1]
        return self._app_name or False

    @logged
    def _set_app(self):
        if self._platform == 'Android':
            suffix = 'apk'
        elif self._platform == 'Ios':
            suffix = 'ipa'
        else:
            suffix = 'app'

        apps = os.listdir(self._file_dir_path)
        if len(apps):
            for app in apps:
                if self._app_version:
                    you_app = re.findall(
                        re.compile('.*{}.*{}.{}'.format(self._app_version, self._env, suffix), re.S), app)
                    if len(you_app) > 1:
                        raise AppFileNotOnlyException("{}文件不唯一".format(suffix))
                    elif len(you_app) == 1:
                        self._app_path = os.path.join(self._file_dir_path, you_app[0])
                        LOGGER.info("找到{}文件，路径是：{}".format(suffix, self._app_path))
                    else:
                        continue
                else:
                    you_app = re.findall(re.compile('.*{}.{}'.format(self._env, suffix), re.S), app)
                    if len(you_app) > 1:
                        raise AppFileNotOnlyException("{}文件不唯一".format(suffix))
                    elif len(you_app) == 1:
                        self._app_path = os.path.join(self._file_dir_path, you_app[0])
                        LOGGER.info("找到{}文件，路径是：{}".format(suffix, self._app_path))
                    else:
                        continue
        else:
            raise AppFileNotFoundException("没找到任何apk文件!")


if __name__ == '__main__':
    apk1 = Apps("android")
    print(apk1.path)
    print(apk1.name)
    app1 = Apps()
    print(app1.name)
    print(app1.path)
