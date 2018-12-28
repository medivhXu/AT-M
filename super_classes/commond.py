#!/usr/bin/env python3
import sys
import abc
import subprocess
from atm.log import LOGGER


class Command(metaclass=abc.ABCMeta):
    def __init__(self):
        self.sys = None

    @classmethod
    def kill_port(cls, pid):
        r = cls.run_cmd('kill -9 {}'.format(pid))
        return r

    @classmethod
    def find_used_port(cls, port):
        if sys.platform == 'darwin' or sys.platform == 'linux':
            r = cls.run_cmd('lsof -i tcp:{}'.format(port))
            return r
        else:
            r = cls.run_cmd('tasklist|findstr "{}"'.format(port))
            return r

    @abc.abstractmethod
    def check_port(self, port):
        raise NotImplementedError

    @abc.abstractmethod
    def start_appium(self, add, port, bootstrap_port, chrome_port, udid):
        raise NotImplementedError

    @abc.abstractmethod
    def show_sdk(self):
        raise NotImplementedError

    @classmethod
    def run_cmd(cls, command):
        try:
            res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            res.wait()
            result = res.stdout.readlines()
        except subprocess.CalledProcessError as e:
            LOGGER.warning("命令运行失败！{}".format(e))
            raise e
        return result
