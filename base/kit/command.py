#!/usr/bin/env python3
"""
@author: Medivh Xu
@file: command.py
@time: 2020-03-20 14:10
"""
import re
import sys
import subprocess
import abc
from loguru import logger


class Command(metaclass=abc.ABCMeta):
    """鸡肋，用以执行系统命令"""

    @classmethod
    def start_appium(cls, udid, addr='127.0.0.1', port=4727, bootstrap_port=4728, chrome_port=9519):
        cls.run_cmd(
            'appium -a {addr} -p {port} -bp {bootstrap_port} --chromedriver-port {chrome_port} -U {udid} --session-override'
                .format(addr, port, bootstrap_port, chrome_port, udid))

    @classmethod
    def stop_appium(cls, port, command_re='appium'):
        cls.kill_port(cls.find_pid_occupies_port(port=port, command_re=command_re))

    @classmethod
    def kill_port(cls, pid):
        r = cls.run_cmd('kill -9 {}'.format(pid))
        return r

    @classmethod
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
    def check_appium_version(cls):
        appium_version = cls.run_cmd('appium -v')
        if appium_version:
            return bytes.decode(appium_version[0])
        else:
            raise EnvironmentError("请检查appium配置！")

    @classmethod
    def get_pid_by_keyword(cls, keyword):
        r = cls.run_cmd('ps -ef |grep adb|grep -v grep |awk "{print $2}"'.format(keyword))
        return r

    @classmethod
    def run_cmd(cls, command):
        try:
            logger.info("{} run command: {}".format(cls.__name__, command))
            res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            res.wait()
            result = res.stdout.readlines()
        except subprocess.CalledProcessError as e:
            logger.warning("命令运行失败！{}".format(e))
            raise e
        return result
