#!/usr/bin/env python3
import re
import sys
import subprocess
import abc
from atm.log import LOGGER, logged


class Command(metaclass=abc.ABCMeta):
    """鸡肋，用以执行系统命令"""
    @abc.abstractmethod
    def start(self):
        ...

    @abc.abstractmethod
    def stop(self):
        ...

    def start_appium(self, udid, add='127.0.0.1', port=4727, bootstrap_port=4728, chrome_port=9519):
        self.run_cmd(
            'appium -a {add} -p {port} -bp {bootstrap_port} --chromedriver-port {chrome_port} -U {udid} --session-override'
                .format(add, port, bootstrap_port, chrome_port, udid))

    @classmethod
    def stop_appium(cls, port, command_re='appium'):
        cls.kill_port(cls.find_pid_occupies_port(port=port, command_re=command_re))

    @classmethod
    @logged
    def kill_port(cls, pid):
        r = cls.run_cmd('kill -9 {}'.format(pid))
        return r

    @classmethod
    @logged
    def find_pid_occupies_port(cls, port, command_re):
        if sys.platform == 'darwin' or sys.platform == 'linux':
            r = cls.run_cmd('lsof -i tcp:{}'.format(port))
            if iter(r):
                for i in r:
                    re_r = re.compile('{}.* '.format(command_re), re.S)
                    a = re.findall(re_r, i.decode())
                    if len(a):
                        c = [j for j in a[0].split(' ') if len(j)]
                        return c[1]
            else:
                re_r = re.compile('{}.* '.format(command_re), re.S)
                a = re.findall(re_r, r.decode())
                if len(a):
                    c = [j for j in a[0].split(' ') if len(j)]
                    return c[1]
        else:
            r = cls.run_cmd('tasklist|findstr "{}"'.format(port))
            if iter(r):
                for i in r:
                    re_r = re.compile('{}.* '.format(command_re), re.S)
                    a = re.findall(re_r, i.decode())
                    if len(a):
                        c = [j for j in a[0].split(' ') if len(j)]
                        return c[1]
            else:
                re_r = re.compile('{}.* '.format(command_re), re.S)
                a = re.findall(re_r, r.decode())
                if len(a):
                    c = [j for j in a[0].split(' ') if len(j)]
                    return c[1]

    @classmethod
    def echo_path(cls):
        r = cls.run_cmd('echo $PATH')
        return r

    @classmethod
    @logged
    def run_cmd(cls, command):
        try:
            res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            res.wait()
            result = res.stdout.readlines()
        except subprocess.CalledProcessError as e:
            LOGGER.warning("命令运行失败！{}".format(e))
            raise e
        return result
