#!/usr/bin/env python3
"""
@author: Medivh Xu
@file: imobile_kit.py
@time: 2020-03-20 14:10
"""
from base.kit.command import Command


class IMobile(Command):
    """
    ios libimobiledriver命令管理
    :return
    """
    def __init__(self):
        super(IMobile, self).__init__()
        self.idevice = 'idevce'

    def start(self):
        pass

    def stop(self):
        pass

    def disconnect(self):
        pass

    def devices(self):
        """
        Return device dict
        For example:
        {
            "1002038889199992134bad1234112312": "Tony's iPhone"
        }
        """
        idevice_cmd = ''.join((self.idevice, '_id', ' -l'))
        self.run_cmd(idevice_cmd)
        return idevice_cmd

    def kill_port(self, port):
        raise NotImplementedError

    def check_port(self, port):
        raise NotImplementedError

    def start_appium(self, udid, add='127.0.0.1', port=4727, bootstrap_port=4728, chrome_port=9519):
        pass

    def show_sdk(self):
        raise NotImplementedError
